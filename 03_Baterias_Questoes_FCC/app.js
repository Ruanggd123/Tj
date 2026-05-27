document.addEventListener('DOMContentLoaded', () => {
    let allQuestions = [];
    let filteredQuestions = [];
    let currentFilter = 'all';
    let currentPage = 1;
    const questionsPerPage = 30;

    function formatText(text) {
        if (!text) return '';
        
        let cleaned = text
            .replace(/\\land/g, ' ∧ ')
            .replace(/\\lor/g, ' ∨ ')
            .replace(/\\sim/g, ' ~ ')
            .replace(/\\rightarrow/g, ' → ')
            .replace(/\\leftrightarrow/g, ' ↔ ')
            .replace(/\\neg/g, ' ¬ ')
            .replace(/\\leq?/g, ' ≤ ')
            .replace(/\\geq?/g, ' ≥ ')
            .replace(/\\neq?/g, ' ≠ ')
            .replace(/\\times/g, ' × ')
            .replace(/\\div/g, ' ÷ ')
            .replace(/\\cdot/g, ' · ')
            .replace(/\\approx/g, ' ≈ ')
            .replace(/\\frac\{([^\}]+)\}\{([^\}]+)\}/g, '$1 / $2')
            .replace(/\\text\{([^\}]+)\}/g, '$1')
            .replace(/\$/g, '');

        let html = cleaned
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');

        // 1. Code blocks: ```[lang] ... ```
        html = html.replace(/```(?:[a-zA-Z0-9]+)?\n([\s\S]*?)\n```/g, (match, code) => {
            return `<pre><code>${code}</code></pre>`;
        });

        // 2. Inline code: `code`
        html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

        // 3. Tables:
        const lines = html.split('\n');
        let inTable = false;
        let tableHtml = '';
        let resultLines = [];
        let rowCount = 0;

        for (let i = 0; i < lines.length; i++) {
            let line = lines[i].trim();
            if (line.startsWith('|')) {
                if (!inTable) {
                    inTable = true;
                    tableHtml = '<table>';
                    rowCount = 0;
                }
                
                if (line.match(/^\|[\s\-\|]+$/)) {
                    continue; 
                }
                
                const cells = line.split('|').slice(1, -1).map(c => c.trim());
                tableHtml += '<tr>';
                cells.forEach(cell => {
                    const tag = (rowCount === 0) ? 'th' : 'td';
                    tableHtml += `<${tag}>${cell}</${tag}>`;
                });
                tableHtml += '</tr>';
                rowCount++;
            } else {
                if (inTable) {
                    inTable = false;
                    tableHtml += '</table>';
                    resultLines.push(tableHtml);
                    tableHtml = '';
                }
                resultLines.push(line);
            }
        }
        if (inTable) {
            tableHtml += '</table>';
            resultLines.push(tableHtml);
        }

        html = resultLines.join('\n');

        // 4. Bold: **text**
        html = html.replace(/\*\*([\s\S]*?)\*\*/g, '<strong>$1</strong>');

        // 5. Line breaks (masking pre and table)
        const blocks = [];
        html = html.replace(/(<pre>[\s\S]*?<\/pre>|<table>[\s\S]*?<\/table>)/g, (match) => {
            blocks.push(match);
            return `__BLOCK_PLACEHOLDER_${blocks.length - 1}__`;
        });

        html = html.replace(/\n/g, '<br>');

        html = html.replace(/__BLOCK_PLACEHOLDER_(\d+)__/g, (match, idx) => {
            return blocks[parseInt(idx)];
        });

        return html;
    }
    
    function getWeekNumber(dayId) {
        const match = dayId.match(/^dia_(\d+)_(\d+)$/);
        if (!match) return null;
        const day = parseInt(match[1]);
        const month = parseInt(match[2]) - 1;
        const year = 2026;
        const date = new Date(year, month, day);
        
        const startDate = new Date(2026, 4, 16); // May 16, 2026
        
        const diffTime = date - startDate;
        if (diffTime < 0) return 1;
        
        const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
        
        if (diffDays < 9) {
            return 1;
        } else {
            return Math.floor((diffDays - 9) / 7) + 2;
        }
    }

    function shortenDayTitle(title) {
        if (!title) return '';
        return title
            .replace('Segunda-feira', 'Seg')
            .replace('Terça-feira', 'Ter')
            .replace('Quarta-feira', 'Qua')
            .replace('Quinta-feira', 'Qui')
            .replace('Sexta-feira', 'Sex')
            .replace('Sábado', 'Sáb')
            .replace('Domingo', 'Dom');
    }

    // DOM Elements
    const qContainer = document.getElementById('questions-container');
    const dropdownWrapper = document.querySelector('.dropdown-wrapper');
    const daySelectorTrigger = document.getElementById('day-selector-trigger');
    const daySelectorDropdown = document.getElementById('day-selector-dropdown');
    const weeksGrid = document.getElementById('weeks-grid');
    const btnSelectAll = document.getElementById('btn-select-all');
    const btnPrevDay = document.getElementById('btn-prev-day');
    const btnNextDay = document.getElementById('btn-next-day');
    const selectedDayLabel = document.getElementById('selected-day-label');

    const totalQElement = document.getElementById('stat-total');
    const totalDaysElement = document.getElementById('stat-days');
    const solvedElement = document.getElementById('stat-solved');
    const btnPrev = document.getElementById('btn-prev');
    const btnNext = document.getElementById('btn-next');
    const pageInfo = document.getElementById('page-info');
    const pagination = document.getElementById('pagination');

    // Memory cache for questions by day
    const loadedDays = new Map();
    let indexData = [];

    // Local Storage persistence
    let answeredQuestions = JSON.parse(localStorage.getItem('tjce_answered_questions') || '{}');
    let completedDays = new Set(JSON.parse(localStorage.getItem('tjce_completed_days') || '[]'));

    // Init
    migratePre18();
    fetchIndex();
    setupDropdownEvents();

    function setupDropdownEvents() {
        if (daySelectorTrigger && dropdownWrapper) {
            daySelectorTrigger.onclick = (e) => {
                e.stopPropagation();
                dropdownWrapper.classList.toggle('open');
            };

            document.addEventListener('click', (e) => {
                if (!dropdownWrapper.contains(e.target)) {
                    dropdownWrapper.classList.remove('open');
                }
            });

            if (daySelectorDropdown) {
                daySelectorDropdown.onclick = (e) => {
                    e.stopPropagation();
                };
            }
        }

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                closeDropdown();
            }
        });

        if (btnSelectAll) {
            btnSelectAll.onclick = (e) => {
                e.stopPropagation();
                applyFilter('all');
                closeDropdown();
            };
        }

        if (btnPrevDay) {
            btnPrevDay.onclick = () => {
                if (currentFilter === 'all') return;
                const index = indexData.findIndex(d => d.day_id === currentFilter);
                if (index === 0) {
                    applyFilter('all');
                } else if (index > 0) {
                    applyFilter(indexData[index - 1].day_id);
                }
            };
        }

        if (btnNextDay) {
            btnNextDay.onclick = () => {
                if (currentFilter === 'all') {
                    if (indexData.length > 0) {
                        applyFilter(indexData[0].day_id);
                    }
                } else {
                    const index = indexData.findIndex(d => d.day_id === currentFilter);
                    if (index >= 0 && index < indexData.length - 1) {
                        applyFilter(indexData[index + 1].day_id);
                    }
                }
            };
        }
    }

    function closeDropdown() {
        if (dropdownWrapper) {
            dropdownWrapper.classList.remove('open');
        }
    }

    async function migratePre18() {
        if (!localStorage.getItem('tjce_pre_18_marked')) {
            const daysToMark = ['dia_16_05', 'dia_17_05', 'dia_18_05'];
            daysToMark.forEach(day => completedDays.add(day));
            localStorage.setItem('tjce_completed_days', JSON.stringify([...completedDays]));

            try {
                const responses = await Promise.all([
                    fetch('dia_16_05_questoes.json').then(r => r.ok ? r.json() : []),
                    fetch('dia_17_05_questoes.json').then(r => r.ok ? r.json() : []),
                    fetch('dia_18_05_questoes.json').then(r => r.ok ? r.json() : [])
                ]);

                responses.flat().forEach(q => {
                    const qKey = `q_${q.day_id}_${q.source.replace(/[^a-zA-Z0-9]/g, '_')}`;
                    answeredQuestions[qKey] = {
                        selected: q.answer,
                        isCorrect: true
                    };
                });

                localStorage.setItem('tjce_answered_questions', JSON.stringify(answeredQuestions));
                localStorage.setItem('tjce_pre_18_marked', 'true');
                
                if (indexData && indexData.length > 0) {
                    setupFilters();
                    updateStats();
                    renderPage();
                }
            } catch (err) {
                console.error('Erro na migração das questões pré-18/05:', err);
            }
        }
    }

    async function fetchIndex() {
        try {
            qContainer.innerHTML = '<div class="loading">Carregando índice de questões...</div>';
            const response = await fetch('questoes_index.json');
            if (!response.ok) throw new Error('Falha ao carregar o índice de questões');
            
            indexData = await response.json();
            
            setupFilters();
            updateStats();
            
            // Default: load all questions
            await loadDayData('all');
            renderPage();
            
        } catch (error) {
            console.error(error);
            qContainer.innerHTML = `<div class="loading" style="color: var(--error)">
                Erro ao carregar as questões. Você está rodando via servidor local (Live Server)?<br>
                ${error.message}
            </div>`;
        }
    }

    async function loadDayData(dayId) {
        if (dayId === 'all') {
            const promises = indexData.map(item => fetchDayFile(item.day_id, item.filename));
            const results = await Promise.all(promises);
            allQuestions = results.flat();
            filteredQuestions = [...allQuestions];
        } else {
            const item = indexData.find(d => d.day_id === dayId);
            if (item) {
                const dayQuestions = await fetchDayFile(item.day_id, item.filename);
                filteredQuestions = dayQuestions;
            }
        }
    }

    async function fetchDayFile(dayId, filename) {
        if (loadedDays.has(dayId)) {
            return loadedDays.get(dayId);
        }
        try {
            const res = await fetch(filename);
            if (!res.ok) throw new Error(`Falha ao carregar ${filename}`);
            const data = await res.json();
            loadedDays.set(dayId, data);
            return data;
        } catch (err) {
            console.error(err);
            return [];
        }
    }

    function setupFilters() {
        if (!weeksGrid) return;
        weeksGrid.innerHTML = '';
        
        // Group by week
        const weeksMap = new Map();
        indexData.forEach(item => {
            const weekNum = getWeekNumber(item.day_id);
            if (!weeksMap.has(weekNum)) {
                weeksMap.set(weekNum, []);
            }
            weeksMap.get(weekNum).push(item);
        });
        
        // Sort weeks
        const sortedWeeks = Array.from(weeksMap.keys()).sort((a, b) => a - b);
        
        sortedWeeks.forEach(weekNum => {
            const weekRow = document.createElement('div');
            weekRow.className = 'week-row';
            
            const weekTitle = document.createElement('div');
            weekTitle.className = 'week-title';
            weekTitle.textContent = `Semana ${weekNum}`;
            weekRow.appendChild(weekTitle);
            
            const weekDays = document.createElement('div');
            weekDays.className = 'week-days';
            
            weeksMap.get(weekNum).forEach(item => {
                const btn = document.createElement('button');
                btn.className = 'btn-filter-compact';
                if (completedDays.has(item.day_id)) {
                    btn.classList.add('day-completed');
                }
                if (currentFilter === item.day_id) {
                    btn.classList.add('active');
                }
                btn.textContent = shortenDayTitle(item.day_title);
                btn.onclick = (e) => {
                    e.stopPropagation();
                    applyFilter(item.day_id);
                    closeDropdown();
                };
                weekDays.appendChild(btn);
            });
            
            weekRow.appendChild(weekDays);
            weeksGrid.appendChild(weekRow);
        });
        
        // Update Ver Todas class
        if (btnSelectAll) {
            if (currentFilter === 'all') {
                btnSelectAll.classList.add('active');
            } else {
                btnSelectAll.classList.remove('active');
            }
        }
        
        // Update labels and navigation
        updateSelectorLabel();
        updateNavButtons();
    }

    function updateSelectorLabel() {
        if (!selectedDayLabel) return;
        if (currentFilter === 'all') {
            selectedDayLabel.textContent = 'Ver Todas as Questões';
        } else {
            const item = indexData.find(d => d.day_id === currentFilter);
            if (item) {
                selectedDayLabel.textContent = item.day_title;
            } else {
                selectedDayLabel.textContent = currentFilter;
            }
        }
    }

    function updateNavButtons() {
        if (!btnPrevDay || !btnNextDay) return;
        if (currentFilter === 'all') {
            btnPrevDay.disabled = true;
            btnNextDay.disabled = indexData.length === 0;
        } else {
            const index = indexData.findIndex(d => d.day_id === currentFilter);
            btnPrevDay.disabled = false;
            btnNextDay.disabled = index === indexData.length - 1;
        }
    }

    async function applyFilter(dayId) {
        currentFilter = dayId;
        currentPage = 1;

        setupFilters();

        qContainer.innerHTML = '<div class="loading">Carregando questões...</div>';
        await loadDayData(dayId);
        renderPage();
    }

    function updateStats() {
        const total = indexData.reduce((acc, item) => acc + item.count, 0);
        totalQElement.textContent = total;
        totalDaysElement.textContent = `${indexData.length} dias`;
        
        // Solved questions count
        const solvedCount = Object.keys(answeredQuestions).length;
        const percentage = total > 0 ? ((solvedCount / total) * 100).toFixed(0) : 0;
        solvedElement.textContent = `${percentage}%`;
    }

    function toggleDayCompletion(dayId) {
        if (completedDays.has(dayId)) {
            completedDays.delete(dayId);
        } else {
            completedDays.add(dayId);
        }
        localStorage.setItem('tjce_completed_days', JSON.stringify([...completedDays]));
        setupFilters();
        renderPage();
    }

    function resetDayQuestions(dayId) {
        // Remove all keys matching `q_${dayId}_`
        const prefix = `q_${dayId}_`;
        Object.keys(answeredQuestions).forEach(key => {
            if (key.startsWith(prefix)) {
                delete answeredQuestions[key];
            }
        });
        
        // Also unmark day completion
        completedDays.delete(dayId);
        
        localStorage.setItem('tjce_answered_questions', JSON.stringify(answeredQuestions));
        localStorage.setItem('tjce_completed_days', JSON.stringify([...completedDays]));
        
        setupFilters();
        updateStats();
        renderPage();
    }

    async function markAllDayQuestions(dayId) {
        // Load the questions for this day if not loaded yet
        qContainer.innerHTML = '<div class="loading">Carregando questões para marcar...</div>';
        await loadDayData(dayId);
        
        filteredQuestions.forEach(q => {
            const qKey = `q_${q.day_id}_${q.source.replace(/[^a-zA-Z0-9]/g, '_')}`;
            answeredQuestions[qKey] = {
                selected: q.answer,
                isCorrect: true
            };
        });
        
        // Also mark day completion
        completedDays.add(dayId);
        
        localStorage.setItem('tjce_answered_questions', JSON.stringify(answeredQuestions));
        localStorage.setItem('tjce_completed_days', JSON.stringify([...completedDays]));
        
        setupFilters();
        updateStats();
        renderPage();
    }

    function renderPage() {
        qContainer.innerHTML = '';
        
        // Render day completion banner if filtering a specific day
        if (currentFilter !== 'all') {
            const isCompleted = completedDays.has(currentFilter);
            const item = indexData.find(d => d.day_id === currentFilter);
            const banner = document.createElement('div');
            banner.className = 'day-completion-banner';
            banner.innerHTML = `
                <div>
                    <span>Dia de Estudos: <strong>${item ? item.day_title : currentFilter}</strong></span>
                </div>
                <div style="display: flex; gap: 10px; align-items: center; flex-wrap: wrap;">
                    <button class="btn-complete-day ${isCompleted ? 'is-completed' : ''}" id="btn-complete-day">
                        ${isCompleted ? '✓ Dia Concluído' : 'Marcar Dia como Concluído'}
                    </button>
                    <button class="btn-mark-all-day" id="btn-mark-all-day" title="Marcar todas as questões deste dia como corretas">
                        ✅ Marcar Todas como Feitas
                    </button>
                    <button class="btn-reset-day" id="btn-reset-day" title="Limpar respostas deste dia para refazer">
                        🔄 Refazer Questões
                    </button>
                </div>
            `;
            qContainer.appendChild(banner);
            
            banner.querySelector('#btn-complete-day').onclick = () => toggleDayCompletion(currentFilter);
            banner.querySelector('#btn-mark-all-day').onclick = () => {
                if (confirm('Deseja realmente marcar todas as questões deste dia como respondidas corretas?')) {
                    markAllDayQuestions(currentFilter);
                }
            };
            banner.querySelector('#btn-reset-day').onclick = () => {
                if (confirm('Deseja realmente limpar suas respostas deste dia para refazê-las?')) {
                    resetDayQuestions(currentFilter);
                }
            };
        }

        const totalPages = Math.ceil(filteredQuestions.length / questionsPerPage);
        
        if (filteredQuestions.length === 0) {
            qContainer.innerHTML += `<div class="loading">Nenhuma questão encontrada.</div>`;
            pagination.style.display = 'none';
            return;
        }

        const startIndex = (currentPage - 1) * questionsPerPage;
        const endIndex = Math.min(startIndex + questionsPerPage, filteredQuestions.length);
        
        const pageQuestions = filteredQuestions.slice(startIndex, endIndex);

        pageQuestions.forEach((q, index) => {
            const card = createQuestionCard(q, startIndex + index + 1);
            qContainer.appendChild(card);
        });

        // Update Pagination UI
        if (totalPages > 1) {
            pagination.style.display = 'flex';
            pageInfo.textContent = `Página ${currentPage} de ${totalPages}`;
            btnPrev.disabled = currentPage === 1;
            btnNext.disabled = currentPage === totalPages;
        } else {
            pagination.style.display = 'none';
        }

        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function createQuestionCard(q, displayNum) {
        const card = document.createElement('div');
        card.className = 'question-card';
        card.dataset.id = q.id;

        const qKey = `q_${q.day_id}_${q.source.replace(/[^a-zA-Z0-9]/g, '_')}`;
        const savedAnswer = answeredQuestions[qKey];

        if (savedAnswer) {
            card.classList.add('answered');
        }

        const explanationHtml = q.explanation ? formatText(q.explanation) : 'Sem explicação disponível.';

        let contextHtml = '';
        if (q.context) {
            contextHtml = `<div class="q-context" style="margin-bottom: 20px; padding: 15px; background: rgba(255,255,255,0.03); border-left: 3px solid var(--primary); border-radius: 4px;">
                ${formatText(q.context)}
            </div>`;
        }

        let optionsHtml = '';
        for (const [letter, text] of Object.entries(q.options)) {
            const isCorrect = letter === q.answer;
            let optionClasses = 'option-item';
            if (isCorrect) {
                optionClasses += ' is-correct-answer';
            }
            if (savedAnswer && savedAnswer.selected === letter) {
                optionClasses += ' selected';
                optionClasses += isCorrect ? ' correct' : ' wrong';
            }
            optionsHtml += `
                <div class="${optionClasses}" data-letter="${letter}">
                    <div class="option-letter">${letter}</div>
                    <div class="option-text">${formatText(text)}</div>
                </div>
            `;
        }

        card.innerHTML = `
            <div class="q-header">
                <div class="q-theme">${q.theme}</div>
                <div class="q-source">#${displayNum} | ${q.source}</div>
            </div>
            ${contextHtml}
            <div class="q-statement">${formatText(q.statement)}</div>
            <div class="options-list">
                ${optionsHtml}
            </div>
            <div class="explanation-box">
                <div class="exp-header">
                    <span>🔑 Gabarito e Explicação</span>
                </div>
                <div class="exp-content">
                    <p><strong>Gabarito Correto: ${q.answer}</strong></p>
                    ${explanationHtml}
                </div>
            </div>
        `;

        // Add event listeners for options
        const optionElements = card.querySelectorAll('.option-item');
        optionElements.forEach(opt => {
            opt.addEventListener('click', function() {
                if (card.classList.contains('answered')) return;
                
                card.classList.add('answered');
                const selectedLetter = this.dataset.letter;
                
                if (selectedLetter === q.answer) {
                    this.classList.add('selected', 'correct');
                } else {
                    this.classList.add('selected', 'wrong');
                }

                // Save to localStorage
                answeredQuestions[qKey] = {
                    selected: selectedLetter,
                    isCorrect: selectedLetter === q.answer
                };
                localStorage.setItem('tjce_answered_questions', JSON.stringify(answeredQuestions));
                updateStats();
            });
        });

        return card;
    }

    // Event Listeners Pagination
    btnPrev.addEventListener('click', () => {
        if (currentPage > 1) {
            currentPage--;
            renderPage();
        }
    });

    btnNext.addEventListener('click', () => {
        const totalPages = Math.ceil(filteredQuestions.length / questionsPerPage);
        if (currentPage < totalPages) {
            currentPage++;
            renderPage();
        }
    });
});
