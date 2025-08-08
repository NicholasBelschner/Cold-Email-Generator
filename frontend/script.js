// API configuration
const API_BASE_URL = 'https://cold-email-generator-s6gh.onrender.com'; // Live backend URL

// DOM elements
const emailForm = document.getElementById('emailForm');
const generateBtn = document.getElementById('generateBtn');
const resultContainer = document.getElementById('result');
const emailContent = document.getElementById('emailContent');
const copyBtn = document.getElementById('copyBtn');
const regenerateBtn = document.getElementById('regenerateBtn');

// Form submission handler
emailForm.addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Show loading state
    setLoadingState(true);
    
    try {
        // Get form data
        const formData = new FormData(e.target);
        const data = Object.fromEntries(formData);
        
        // Validate required fields
        if (!validateForm(data)) {
            setLoadingState(false);
            return;
        }
        
        // Call API
        const response = await fetch(`${API_BASE_URL}/generate-email`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const result = await response.json();
        
        // Display result
        displayEmail(result.email);
        
        // Track email generation
        if (typeof gtag !== 'undefined') {
            gtag('event', 'email_generated', {
                'event_category': 'engagement',
                'event_label': data.goal
            });
        }
        
    } catch (error) {
        console.error('Error generating email:', error);
        showError('Failed to generate email. Please try again.');
    } finally {
        setLoadingState(false);
    }
});

// Regenerate button handler
regenerateBtn.addEventListener('click', function() {
    // Scroll to top and trigger form submission
    window.scrollTo({ top: 0, behavior: 'smooth' });
    emailForm.dispatchEvent(new Event('submit'));
});

// Copy button handler
copyBtn.addEventListener('click', async function() {
    try {
        await navigator.clipboard.writeText(emailContent.textContent);
        
        // Track copy action
        if (typeof gtag !== 'undefined') {
            gtag('event', 'email_copied', {
                'event_category': 'engagement',
                'event_label': 'copy_email'
            });
        }
        
        // Show success feedback
        copyBtn.classList.add('copied');
        copyBtn.textContent = '📋 Copied!';
        
        // Reset after 2 seconds
        setTimeout(() => {
            copyBtn.classList.remove('copied');
            copyBtn.textContent = '📋 Copy Email';
        }, 2000);
        
    } catch (err) {
        console.error('Failed to copy: ', err);
        showError('Failed to copy email to clipboard');
    }
});

// Helper functions
function setLoadingState(isLoading) {
    const btnText = generateBtn.querySelector('.btn-text');
    const btnLoading = generateBtn.querySelector('.btn-loading');
    
    if (isLoading) {
        generateBtn.classList.add('loading');
        generateBtn.disabled = true;
        btnText.style.display = 'none';
        btnLoading.style.display = 'inline';
    } else {
        generateBtn.classList.remove('loading');
        generateBtn.disabled = false;
        btnText.style.display = 'inline';
        btnLoading.style.display = 'none';
    }
}

function validateForm(data) {
    const requiredFields = ['company_name', 'target_industry', 'goal', 'product_description', 'tone'];
    
    for (const field of requiredFields) {
        if (!data[field] || data[field].trim() === '') {
            showError(`Please fill in the ${field.replace('_', ' ')} field.`);
            return false;
        }
    }
    
    return true;
}

function displayEmail(email) {
    emailContent.textContent = email;
    resultContainer.style.display = 'block';
    
    // Scroll to result
    resultContainer.scrollIntoView({ behavior: 'smooth' });
}

function showError(message) {
    // Create error notification
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-notification';
    errorDiv.textContent = message;
    errorDiv.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: #ef4444;
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        z-index: 1000;
        font-weight: 500;
    `;
    
    document.body.appendChild(errorDiv);
    
    // Remove after 5 seconds
    setTimeout(() => {
        errorDiv.remove();
    }, 5000);
}

// Add some nice UX touches
document.addEventListener('DOMContentLoaded', function() {
    // Add focus effects to form inputs
    const inputs = document.querySelectorAll('input, select, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.style.transform = 'scale(1.02)';
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.style.transform = 'scale(1)';
        });
    });
    
    // Add character counter for textarea
    const textarea = document.getElementById('product_description');
    textarea.addEventListener('input', function() {
        const maxLength = 500;
        const currentLength = this.value.length;
        
        if (currentLength > maxLength) {
            this.value = this.value.substring(0, maxLength);
        }
    });
});

// Handle API URL for different environments
if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    // Local development
    API_BASE_URL = 'http://localhost:8000';
} else {
    // Production - live backend URL
    API_BASE_URL = 'https://cold-email-generator-s6gh.onrender.com';
} 