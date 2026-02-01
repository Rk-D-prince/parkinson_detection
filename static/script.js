document.addEventListener('DOMContentLoaded', () => {
    // Add a feature to quickly fill sample data for testing
    const header = document.querySelector('header');
    const demoBtn = document.createElement('button');
    demoBtn.innerText = "Fill Sample Healthy Data";
    demoBtn.style = "margin-top: 10px; cursor: pointer; background: none; border: 1px solid #cbd5e1; padding: 5px 10px; border-radius: 5px; font-size: 0.7rem;";
    
    demoBtn.onclick = () => {
        const samples = {
            'fo': 119.99, 'fhi': 157.30, 'flo': 74.99, 'jitter_percent': 0.007, 
            'jitter_abs': 0.00007, 'rap': 0.0037, 'ppq': 0.0055, 'ddp': 0.011,
            'shimmer': 0.043, 'shimmer_db': 0.426, 'apq3': 0.021, 'apq5': 0.031,
            'apq': 0.029, 'dda': 0.065, 'nhr': 0.022, 'hnr': 21.03, 'rpde': 0.414,
            'dfa': 0.815, 'spread1': -4.813, 'spread2': 0.266, 'd2': 2.301, 'ppe': 0.284
        };
        
        Object.keys(samples).forEach(key => {
            const input = document.querySelector(`input[name="${key}"]`);
            if(input) input.value = samples[key];
        });
    };
    
    header.appendChild(demoBtn);
});