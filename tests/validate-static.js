'use strict';

const fs = require('fs');
const vm = require('vm');
const path = require('path');

const root = path.resolve(__dirname, '..');
const current = fs.readFileSync(path.join(root, 'presentation.html'), 'utf8');
const original = fs.readFileSync(path.join(root, 'backup', 'presentation-original.html'), 'utf8');
const results = [];

function check(id, condition, evidence) {
    results.push({ id, passed: Boolean(condition), evidence });
}

function extractSlides(html) {
    const slides = [];
    const startPattern = /<div class="slide slide-\d+(?: active)?">/g;
    let startMatch;
    while ((startMatch = startPattern.exec(html))) {
        const tokenPattern = /<div\b[^>]*>|<\/div>/g;
        tokenPattern.lastIndex = startMatch.index;
        let depth = 0;
        let token;
        while ((token = tokenPattern.exec(html))) {
            if (token[0].startsWith('</')) depth--;
            else depth++;
            if (depth === 0) {
                slides.push(html.slice(startMatch.index, tokenPattern.lastIndex));
                startPattern.lastIndex = tokenPattern.lastIndex;
                break;
            }
        }
    }
    return slides;
}

const currentSlides = extractSlides(current);
const originalSlides = extractSlides(original);
check('T01', currentSlides.length === 19, `${currentSlides.length} slides encontrados`);
check('T01-PRESERVE', JSON.stringify(currentSlides) === JSON.stringify(originalSlides), 'Blocos dos slides comparados byte a byte com o backup');

const scripts = [...current.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/gi)].map(match => match[1]);
let syntaxError = '';
scripts.forEach((source, index) => {
    try { new vm.Script(source, { filename: `inline-${index + 1}.js` }); }
    catch (error) { syntaxError += `${error.message}; `; }
});
check('JS-SYNTAX', syntaxError === '', syntaxError || `${scripts.length} scripts inline compilados`);
check('OFFLINE', !/https?:\/\//i.test(current), 'Nenhuma URL HTTP(S) no HTML');
check('QUIZ-COUNT', (current.match(/question:'[^']+'/g) || []).length === 3, 'Três perguntas na estrutura JavaScript');
check('QUIZ-OPTIONS', (current.match(/options:\[/g) || []).length === 3 && (current.match(/correctIndex:2/g) || []).length === 3, 'Três conjuntos de quatro opções e respostas oficiais C');
check('TIMER', current.includes('quizRemaining = 60') && current.includes('100 + remaining'), 'Timer de 60s e fórmula 100 + segundos restantes');
check('LAYERS', ['homeLayer','universeLayer','quizLayer','helpLayer','notesLayer'].every(id => current.includes(`id="${id}"`)), 'Cinco camadas principais presentes');
check('A11Y', current.includes('aria-live="assertive"') && current.includes('aria-modal="true"') && current.includes('prefers-reduced-motion'), 'ARIA live, diálogos e movimento reduzido presentes');
check('STORAGE', ['lastSlide','visitedSlides','soundEnabled','reducedMotion','presenterNotes','lastQuizResult'].every(key => current.includes(`'${key}'`)), 'Todas as chaves persistentes implementadas');

results.forEach(result => console.log(`${result.passed ? 'PASS' : 'FAIL'} ${result.id}: ${result.evidence}`));
if (results.some(result => !result.passed)) process.exitCode = 1;
