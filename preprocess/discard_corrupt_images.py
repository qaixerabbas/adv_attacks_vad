from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image

prompt = "Valid image or noise?"

model_id = "vikhyatk/moondream2"
revision = "2024-08-26"
model = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision
)
tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

img_path = "train/arrest/Arrest002/Arrest002_x264_110.png"

image = Image.open(img_path)
enc_image = model.encode_image(image)
print(model.answer_question(enc_image, prompt, tokenizer))