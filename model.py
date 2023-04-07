from transformers import AutoTokenizer, AutoModelWithLMHead, SummarizationPipeline
import torch

if torch.backends.mps.is_available():
    device_name = "mps"
elif torch.cuda().is_available():
    device_name = "cuda"
else:
    device_name = "cpu"


device = torch.device(device_name)

pipeline_python = SummarizationPipeline(
    model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_small_source_code_summarization_python"),
    tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_small_source_code_summarization_python", skip_special_tokens=True),
    device=device
)

pipeline_sql = SummarizationPipeline(
    model=AutoModelWithLMHead.from_pretrained("SEBIS/code_trans_t5_base_source_code_summarization_sql"),
    tokenizer=AutoTokenizer.from_pretrained("SEBIS/code_trans_t5_base_source_code_summarization_sql", skip_special_tokens=True),
    device=device
)

print(f"Hardware Used for the acceleration: {device}")

torch.save(pipeline_python, 'models/model_python.pt')
torch.save(pipeline_sql, 'models/model_sql.pt')

print("Model saved succesfully")

