// ΛambdaCalc - Advanced Math Calculator
// Frontend JavaScript for calculator functionality

class LambdaCalculator {
    constructor() {
        this.currentInput = '0';
        this.previousInput = '';
        this.operator = null;
        this.waitingForOperand = false;
        this.history = [];
        this.currentMode = 'basic';
        
        this.initializeElements();
        this.bindEvents();
        this.loadTheme();
    }

    initializeElements() {
        // Display elements
        this.displayCurrent = document.getElementById('display-current');
        this.displayHistory = document.getElementById('display-history');
        this.resultsContent = document.getElementById('results-content');
        
        // Mode elements
        this.modeButtons = document.querySelectorAll('.mode-btn');
        this.calcModes = document.querySelectorAll('.calc-mode');
        
        // Calculator buttons
        this.numberButtons = document.querySelectorAll('.number-btn');
        this.operatorButtons = document.querySelectorAll('.operator-btn');
        this.functionButtons = document.querySelectorAll('.function-btn');
        this.equalsButton = document.querySelector('.equals-btn');
        
        // Specialized calculator elements
        this.matrixInputs = {
            a: document.getElementById('matrix-a'),
            b: document.getElementById('matrix-b')
        };
        
        this.calculusInputs = {
            function: document.getElementById('function-input'),
            variable: document.getElementById('variable-input'),
            limitPoint: document.getElementById('limit-point'),
            limitDirection: document.getElementById('limit-direction')
        };
        
        this.limitInputs = document.getElementById('limit-inputs');
        
        // Theme toggle
        this.themeToggle = document.getElementById('theme-toggle');
    }

    bindEvents() {
        // Mode switching
        this.modeButtons.forEach(btn => {
            btn.addEventListener('click', (e) => this.switchMode(e.target.dataset.mode));
        });

        // Number buttons
        this.numberButtons.forEach(btn => {
            btn.addEventListener('click', (e) => this.inputNumber(e.target.dataset.number));
        });

        // Operator buttons
        this.operatorButtons.forEach(btn => {
            btn.addEventListener('click', (e) => this.inputOperator(e.target.dataset.operator));
        });

        // Function buttons
        this.functionButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                if (e.target.dataset.action) {
                    this.performAction(e.target.dataset.action);
                } else if (e.target.dataset.function) {
                    this.performFunction(e.target.dataset.function);
                }
            });
        });

        // Equals button
        this.equalsButton.addEventListener('click', () => this.calculate());

        // Matrix operations
        document.querySelectorAll('.matrix-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.performMatrixOperation(e.target.dataset.operation));
        });

        // Calculus operations
        document.querySelectorAll('.calculus-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.performCalculusOperation(e.target.dataset.operation));
        });

        // Theme toggle
        this.themeToggle.addEventListener('click', () => this.toggleTheme());

        // Keyboard support
        document.addEventListener('keydown', (e) => this.handleKeyboard(e));

        // Show/hide limit inputs for calculus
        document.querySelectorAll('.calculus-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                if (e.target.dataset.operation === 'limit') {
                    this.limitInputs.style.display = 'block';
                } else {
                    this.limitInputs.style.display = 'none';
                }
            });
        });
    }

    switchMode(mode) {
        this.currentMode = mode;
        
        // Update mode buttons
        this.modeButtons.forEach(btn => {
            btn.classList.toggle('active', btn.dataset.mode === mode);
        });
        
        // Update calculator modes
        this.calcModes.forEach(calcMode => {
            calcMode.classList.toggle('active', calcMode.id === `${mode}-calc`);
        });
        
        // Clear display when switching modes
        this.clear();
    }

    inputNumber(num) {
        if (this.waitingForOperand) {
            this.currentInput = num;
            this.waitingForOperand = false;
        } else {
            this.currentInput = this.currentInput === '0' ? num : this.currentInput + num;
        }
        this.updateDisplay();
    }

    inputOperator(nextOperator) {
        const inputValue = parseFloat(this.currentInput);

        if (this.previousInput === '') {
            this.previousInput = inputValue;
        } else if (this.operator) {
            const currentValue = this.previousInput || 0;
            const newValue = this.performCalculation(currentValue, inputValue, this.operator);

            this.currentInput = String(newValue);
            this.previousInput = newValue;
            this.updateDisplay();
        }

        this.waitingForOperand = true;
        this.operator = nextOperator;
    }

    performCalculation(firstValue, secondValue, operator) {
        switch (operator) {
            case '+':
                return firstValue + secondValue;
            case '-':
                return firstValue - secondValue;
            case '*':
                return firstValue * secondValue;
            case '/':
                return secondValue !== 0 ? firstValue / secondValue : 0;
            default:
                return secondValue;
        }
    }

    performAction(action) {
        switch (action) {
            case 'clear':
                this.clear();
                break;
            case 'clear-entry':
                this.currentInput = '0';
                this.updateDisplay();
                break;
            case 'backspace':
                this.backspace();
                break;
        }
    }

    performFunction(func) {
        const value = parseFloat(this.currentInput);
        let result;

        switch (func) {
            case 'sin':
                result = Math.sin(value * Math.PI / 180);
                break;
            case 'cos':
                result = Math.cos(value * Math.PI / 180);
                break;
            case 'tan':
                result = Math.tan(value * Math.PI / 180);
                break;
            case 'log':
                result = Math.log10(value);
                break;
            case 'ln':
                result = Math.log(value);
                break;
            case 'sqrt':
                result = Math.sqrt(value);
                break;
            case 'pow':
                result = Math.pow(value, 2);
                break;
            case 'exp':
                result = Math.exp(value);
                break;
            case 'pi':
                result = Math.PI;
                break;
            default:
                return;
        }

        this.currentInput = String(result);
        this.updateDisplay();
        this.addToHistory(`${func}(${value})`, result);
    }

    calculate() {
        const inputValue = parseFloat(this.currentInput);

        if (this.operator && this.previousInput !== '') {
            const newValue = this.performCalculation(this.previousInput, inputValue, this.operator);
            
            this.addToHistory(
                `${this.previousInput} ${this.operator} ${inputValue}`,
                newValue
            );
            
            this.currentInput = String(newValue);
            this.previousInput = '';
            this.operator = null;
            this.waitingForOperand = true;
            this.updateDisplay();
        }
    }

    clear() {
        this.currentInput = '0';
        this.previousInput = '';
        this.operator = null;
        this.waitingForOperand = false;
        this.updateDisplay();
    }

    backspace() {
        if (this.currentInput.length > 1) {
            this.currentInput = this.currentInput.slice(0, -1);
        } else {
            this.currentInput = '0';
        }
        this.updateDisplay();
    }

    updateDisplay() {
        this.displayCurrent.textContent = this.formatNumber(this.currentInput);
        
        if (this.previousInput !== '' && this.operator) {
            this.displayHistory.textContent = `${this.previousInput} ${this.operator}`;
        } else {
            this.displayHistory.textContent = '';
        }
    }

    formatNumber(num) {
        const number = parseFloat(num);
        if (isNaN(number)) return '0';
        
        // Handle very large or very small numbers
        if (Math.abs(number) >= 1e15 || (Math.abs(number) < 1e-10 && number !== 0)) {
            return number.toExponential(6);
        }
        
        // Format with appropriate decimal places
        return number.toString();
    }

    addToHistory(operation, result) {
        const historyItem = {
            operation,
            result: this.formatNumber(result),
            timestamp: new Date().toLocaleTimeString()
        };
        
        this.history.unshift(historyItem);
        
        // Keep only last 10 calculations
        if (this.history.length > 10) {
            this.history = this.history.slice(0, 10);
        }
        
        this.updateResultsPanel();
        this.showSuccessAnimation();
    }

    showSuccessAnimation() {
        // Create a success animation
        const successDiv = document.createElement('div');
        successDiv.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
            padding: 20px 40px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 18px;
            box-shadow: 0 20px 40px rgba(16, 185, 129, 0.3);
            z-index: 1000;
            animation: successPop 2s ease-out forwards;
            pointer-events: none;
        `;
        successDiv.textContent = '✨ Calculation Complete!';
        
        // Add animation keyframes
        const style = document.createElement('style');
        style.textContent = `
            @keyframes successPop {
                0% { opacity: 0; transform: translate(-50%, -50%) scale(0.5); }
                20% { opacity: 1; transform: translate(-50%, -50%) scale(1.1); }
                40% { opacity: 1; transform: translate(-50%, -50%) scale(1); }
                100% { opacity: 0; transform: translate(-50%, -50%) scale(1) translateY(-50px); }
            }
        `;
        document.head.appendChild(style);
        
        document.body.appendChild(successDiv);
        
        // Remove after animation
        setTimeout(() => {
            document.body.removeChild(successDiv);
            document.head.removeChild(style);
        }, 2000);
    }

    showLoadingAnimation(message = 'Processing...') {
        // Remove existing loading animation if any
        const existingLoader = document.getElementById('loading-animation');
        if (existingLoader) {
            existingLoader.remove();
        }

        // Create loading animation
        const loadingDiv = document.createElement('div');
        loadingDiv.id = 'loading-animation';
        loadingDiv.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.95), rgba(118, 75, 162, 0.95));
            backdrop-filter: blur(20px);
            color: white;
            padding: 30px 50px;
            border-radius: 20px;
            font-weight: 600;
            font-size: 16px;
            box-shadow: 0 25px 50px rgba(99, 102, 241, 0.3);
            z-index: 1000;
            text-align: center;
            border: 1px solid rgba(255, 255, 255, 0.2);
        `;
        
        loadingDiv.innerHTML = `
            <div style="margin-bottom: 15px;">
                <div style="width: 40px; height: 40px; border: 3px solid rgba(255,255,255,0.3); border-top: 3px solid white; border-radius: 50%; animation: spin 1s linear infinite; margin: 0 auto;"></div>
            </div>
            <div>${message}</div>
        `;
        
        // Add spin animation
        const style = document.createElement('style');
        style.textContent = `
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        `;
        document.head.appendChild(style);
        
        document.body.appendChild(loadingDiv);
        
        // Store reference for removal
        this.loadingAnimation = loadingDiv;
        this.loadingStyle = style;
    }

    hideLoadingAnimation() {
        if (this.loadingAnimation) {
            document.body.removeChild(this.loadingAnimation);
            this.loadingAnimation = null;
        }
        if (this.loadingStyle) {
            document.head.removeChild(this.loadingStyle);
            this.loadingStyle = null;
        }
    }

    updateResultsPanel() {
        if (this.history.length === 0) {
            this.resultsContent.innerHTML = '<p class="no-results">No calculations yet. Start by entering some numbers!</p>';
            return;
        }

        const resultsHTML = this.history.map(item => `
            <div class="result-item">
                <div class="result-operation">${item.operation}</div>
                <div class="result-value">= ${item.result}</div>
            </div>
        `).join('');

        this.resultsContent.innerHTML = resultsHTML;
    }

    // Matrix Operations
    async performMatrixOperation(operation) {
        try {
            const matrixA = this.matrixInputs.a.value.trim();
            const matrixB = this.matrixInputs.b.value.trim();
            
            if (!matrixA && operation !== 'determinant' && operation !== 'inverse') {
                throw new Error('Please enter Matrix A');
            }
            
            if (!matrixB && (operation === 'add' || operation === 'multiply')) {
                throw new Error('Please enter Matrix B');
            }

            // Show loading animation
            this.showLoadingAnimation('Processing Matrix Operation...');

            const response = await fetch('/api/matrix', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operation: operation,
                    matrixA: matrixA,
                    matrixB: matrixB
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Matrix operation failed');
            }

            const data = await response.json();
            const result = data.result;
            const operationText = this.getMatrixOperationText(operation);

            this.hideLoadingAnimation();
            this.addToHistory(operationText, result);
            this.showResult(result);
        } catch (error) {
            this.hideLoadingAnimation();
            this.showError(`Matrix operation error: ${error.message}`);
        }
    }

    getMatrixOperationText(operation) {
        switch (operation) {
            case 'add': return 'Matrix A + Matrix B';
            case 'multiply': return 'Matrix A × Matrix B';
            case 'inverse': return 'Matrix A⁻¹';
            case 'determinant': return 'det(Matrix A)';
            case 'transpose': return 'Matrix Aᵀ';
            default: return `Matrix ${operation}`;
        }
    }

    parseMatrix(matrixString) {
        if (!matrixString.trim()) {
            throw new Error('Please enter a matrix');
        }
        
        try {
            // Simple matrix parser for format like [[1,2],[3,4]]
            const cleaned = matrixString.replace(/\s/g, '');
            const matrix = JSON.parse(cleaned);
            
            if (!Array.isArray(matrix) || !matrix.every(row => Array.isArray(row))) {
                throw new Error('Invalid matrix format');
            }
            
            return matrix;
        } catch (error) {
            throw new Error('Invalid matrix format. Use format like [[1,2],[3,4]]');
        }
    }

    matrixAdd(a, b) {
        if (a.length !== b.length || a[0].length !== b[0].length) {
            throw new Error('Matrices must have the same dimensions');
        }
        
        return a.map((row, i) => 
            row.map((val, j) => val + b[i][j])
        );
    }

    matrixMultiply(a, b) {
        if (a[0].length !== b.length) {
            throw new Error('Number of columns in A must equal number of rows in B');
        }
        
        const result = [];
        for (let i = 0; i < a.length; i++) {
            result[i] = [];
            for (let j = 0; j < b[0].length; j++) {
                let sum = 0;
                for (let k = 0; k < b.length; k++) {
                    sum += a[i][k] * b[k][j];
                }
                result[i][j] = sum;
            }
        }
        return result;
    }

    matrixInverse(matrix) {
        if (matrix.length !== matrix[0].length) {
            throw new Error('Matrix must be square to find inverse');
        }
        
        // Simple 2x2 matrix inverse
        if (matrix.length === 2) {
            const [[a, b], [c, d]] = matrix;
            const det = a * d - b * c;
            
            if (det === 0) {
                throw new Error('Matrix is singular (determinant is 0)');
            }
            
            return [
                [d / det, -b / det],
                [-c / det, a / det]
            ];
        }
        
        throw new Error('Inverse calculation only supported for 2x2 matrices');
    }

    matrixDeterminant(matrix) {
        if (matrix.length !== matrix[0].length) {
            throw new Error('Matrix must be square to find determinant');
        }
        
        if (matrix.length === 2) {
            const [[a, b], [c, d]] = matrix;
            return a * d - b * c;
        }
        
        throw new Error('Determinant calculation only supported for 2x2 matrices');
    }

    // Calculus Operations
    async performCalculusOperation(operation) {
        try {
            const func = this.calculusInputs.function.value.trim();
            const variable = this.calculusInputs.variable.value.trim() || 'x';
            
            if (!func) {
                throw new Error('Please enter a function');
            }

            // Show loading animation
            this.showLoadingAnimation(`Processing ${operation}...`);

            let result;
            let operationText;

            switch (operation) {
                case 'differentiate':
                    result = await this.differentiate(func, variable);
                    operationText = `d/d${variable}(${func})`;
                    break;
                case 'integrate':
                    result = await this.integrate(func, variable);
                    operationText = `∫${func} d${variable}`;
                    break;
                case 'limit':
                    const point = this.calculusInputs.limitPoint.value.trim();
                    const direction = this.calculusInputs.limitDirection.value;
                    
                    if (!point) {
                        throw new Error('Please enter a limit point');
                    }
                    
                    result = await this.computeLimit(func, variable, point, direction);
                    operationText = `lim(${func}) as ${variable} → ${point}`;
                    break;
            }

            this.hideLoadingAnimation();
            this.addToHistory(operationText, result);
            this.showResult(result);
        } catch (error) {
            this.hideLoadingAnimation();
            this.showError(`Calculus operation error: ${error.message}`);
        }
    }

    async differentiate(func, variable) {
        try {
            const response = await fetch('/api/calculus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operation: 'differentiate',
                    function: func,
                    variable: variable
                })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            return data.result;
        } catch (error) {
            throw new Error('Differentiation failed. Please check your function syntax.');
        }
    }

    async integrate(func, variable) {
        try {
            const response = await fetch('/api/calculus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operation: 'integrate',
                    function: func,
                    variable: variable
                })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            return data.result;
        } catch (error) {
            throw new Error('Integration failed. Please check your function syntax.');
        }
    }

    async computeLimit(func, variable, point, direction) {
        try {
            const response = await fetch('/api/calculus', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    operation: 'limit',
                    function: func,
                    variable: variable,
                    point: point,
                    direction: direction
                })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            return data.result;
        } catch (error) {
            throw new Error('Limit computation failed. Please check your function syntax.');
        }
    }

    showResult(result) {
        // Display result in a user-friendly format
        if (Array.isArray(result)) {
            // Matrix result
            const matrixStr = result.map(row => 
                `[${row.map(val => this.formatNumber(val)).join(', ')}]`
            ).join('\n');
            this.addToHistory('Matrix Result', matrixStr);
        } else {
            this.addToHistory('Result', result);
        }
    }

    showError(message) {
        this.addToHistory('Error', message);
    }

    // Theme Management
    toggleTheme() {
        const currentTheme = document.documentElement.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        document.documentElement.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        
        // Update theme button icon
        const icon = this.themeToggle.querySelector('i');
        icon.className = newTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    }

    loadTheme() {
        const savedTheme = localStorage.getItem('theme') || 'light';
        document.documentElement.setAttribute('data-theme', savedTheme);
        
        const icon = this.themeToggle.querySelector('i');
        icon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
    }

    // Keyboard Support
    handleKeyboard(event) {
        const key = event.key;
        
        // Prevent default for calculator keys
        if ('0123456789+-*/.=c'.includes(key.toLowerCase()) || 
            key === 'Enter' || key === 'Escape' || key === 'Backspace') {
            event.preventDefault();
        }

        if ('0123456789.'.includes(key)) {
            this.inputNumber(key);
        } else if ('+-*/'.includes(key)) {
            this.inputOperator(key);
        } else if (key === 'Enter' || key === '=') {
            this.calculate();
        } else if (key === 'Escape' || key.toLowerCase() === 'c') {
            this.clear();
        } else if (key === 'Backspace') {
            this.backspace();
        }
    }
}

// Initialize the calculator when the DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new LambdaCalculator();
});

// Service Worker registration for PWA capabilities (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then(registration => {
                console.log('SW registered: ', registration);
            })
            .catch(registrationError => {
                console.log('SW registration failed: ', registrationError);
            });
    });
}
