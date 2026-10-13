# text-summarizer-

## workflows

update  config.yaml
update params.yaml
update entity
update configuration manager in src config
update components
update the pipeline
update the main.py
update the app.py



Text Summarization using PEGASUS

An NLP project exploring abstractive text summarization with the PEGASUS sequence-to-sequence transformer and the SAMSum dialogue summarization dataset.

Project status: In progress. Data ingestion and data transformation have been completed. Model-training setup has been started, but a full training run and end-to-end inference have not yet been verified. Evaluation, application, testing, and deployment remain future work.

Overview

Text summarization generates a shorter version of a longer text while retaining its important information. This project is intended to fine-tune a pretrained PEGASUS model for summarizing conversations and to build a pipeline that can generate summaries from input text.

Objectives

Prepare dialogue data for a summarization task.

Configure a pretrained PEGASUS model and tokenizer using Hugging Face Transformers.

Set up a repeatable training workflow.

Evaluate generated summaries and add an inference interface in later stages.

Tech Stack

Language: Python

NLP / Deep learning: Hugging Face Transformers, PyTorch

Model checkpoint: google/pegasus-cnn_dailymail

Dataset: SAMSum

Data / configuration: Datasets, pandas, YAML

Development: Jupyter Notebook and VS Code

Version control: Git and GitHub

How It Works

Data ingestion: Load the source dialogue data.

Data transformation: Prepare the dialogue and summary fields for the model.

Model setup: Load the PEGASUS tokenizer and pretrained sequence-to-sequence model.

Fine-tuning: Train the model on the prepared dataset. This stage has been started but is not confirmed complete.

Evaluation and inference (planned): Generate summaries and evaluate them using appropriate metrics such as ROUGE.

Current Progress

Data ingestion

Data transformation / preprocessing

Initial model-training configuration

Complete and verify model fine-tuning

Save and reload the fine-tuned model and tokenizer

Evaluate generated summaries (for example, with ROUGE)

Complete and test the prediction pipeline

Build a user-facing application

Add automated tests

Verify Docker setup

Verify CI/CD workflow

Deploy the application

Add verified examples, results, and complete usage documentation

The checklist intentionally distinguishes completed work from work that still needs to be tested. Update it as each item is verified.

Training Configuration

Current values in params.yaml:

Parameter

Value

num_train_epochs

1

warmup_steps

500

per_device_train_batch_size

1

weight_decay

0.01

logging_steps

10

evaluation_strategy

steps

eval_steps

500

save_steps

1000000

gradient_accumulation_steps

16

Training has been attempted in a CPU-only environment. Transformer fine-tuning on CPU can be slow, so review dataset size, warmup steps, evaluation frequency, checkpoint saving, and the installed Transformers version before starting a full run. The configuration above documents the current settings; it is not a claim that training has completed successfully.

Repository Structure

Based on the files currently visible in the repository:

text-summarizer-/
├── .github/
├── config/
├── research/
├── src/
│   └── textsummarizer/
├── .gitignore
├── LICENSE
├── README.md
├── app.py
├── dockerfile
├── main.py
├── params.yaml
├── requirements.text
├── setup.py
└── template.py

The app.py file is currently empty in the public repository view, so a working application entry point should not be assumed yet. The dependency file is named requirements.text in the repository; check the filename before using pip commands. If you intend it to be a standard pip requirements file, consider renaming it to requirements.txt and updating any references.

Setup

The complete end-to-end workflow has not yet been verified. The following commands only show a basic Windows PowerShell virtual-environment setup; dependency compatibility and project configuration may require additional work.

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip

After confirming the dependency filename and Python/package compatibility, install the project's dependencies. For a file named requirements.txt, the command would be:

pip install -r requirements.txt

Review config/config.yaml and params.yaml, and confirm the dataset paths and output directories before running the training workflow. Dataset variables created in a Jupyter notebook are not automatically available in a separate PowerShell or Python interpreter session.

Known Limitations

The full PEGASUS fine-tuning run has not been confirmed complete.

CPU-only training can take a long time.

Evaluation metrics and final summary examples have not yet been recorded.

Prediction, app functionality, automated tests, Docker, CI/CD, and deployment require verification or implementation.

Next Steps

Verify the dataset loading code and the number of training and validation examples.

Run a small training experiment before considering a full training run.

Save and reload the model and tokenizer from a known directory.

Generate example summaries and evaluate them with ROUGE.

Finish the prediction pipeline and application.

Add tests and verify containerization and CI/CD.

Document reproducible commands and measured results.

Author

Kavya Banoth
GitHub: @kavyabanoth

This README reflects the progress confirmed so far and should be updated as additional functionality is implemented and tested.
