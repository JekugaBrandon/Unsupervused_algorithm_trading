import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pandas as pd
from pathlib import Path
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def run_notebook(notebook_path):
    """Execute notebook and return the results"""
    logger.info(f"Reading notebook from {notebook_path}")
    
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
    
    logger.info("Executing notebook...")
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': str(Path(notebook_path).parent)}})
    
    # Extract results from the last few cells
    results = {}
    for cell in nb.cells:
        if cell.cell_type == "code" and hasattr(cell, 'outputs'):
            for output in cell.outputs:
                if output.output_type == 'stream':
                    if 'Performance Summary by Regime' in output.text:
                        results['regime_summary'] = output.text
    
    return nb, results

def save_results(notebook, results, output_dir='.'):
    """Save executed notebook and results"""
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save executed notebook
    notebook_output = Path(output_dir) / f'regime_analysis_executed_{timestamp}.ipynb'
    logger.info(f"Saving executed notebook to {notebook_output}")
    with open(notebook_output, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)
    
    # Save results summary
    results_output = Path(output_dir) / f'regime_analysis_results_{timestamp}.json'
    logger.info(f"Saving results to {results_output}")
    with open(results_output, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

def main():
    try:
        notebook_path = 'unsupervised_market_hidden_regime.ipynb'
        output_dir = '.'
        
        # Ensure output directory exists
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Run analysis
        notebook, results = run_notebook(notebook_path)
        
        # Save results
        save_results(notebook, results, output_dir)
        
        logger.info("Analysis complete! Check the output files for results.")
        
    except Exception as e:
        logger.error(f"Error running analysis: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    main()