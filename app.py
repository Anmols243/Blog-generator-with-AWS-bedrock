import boto3
from botocore.config import Config
import json
from datetime import datetime

bedrock = boto3.client(
    "bedrock-runtime",
    region_name = "ap-south-1",
    config = Config(read_timeout=300, retries={'max_attempts':3})
)

def blog_generate(blogtopic: str,
                 max_tokens: int = 400, 
                 temperature: float = 0.7,
                 top_p: float = 0.9) -> str:
    
    try:
        response = bedrock.converse(
            modelId="meta.llama3-8b-instruct-v1:0",
            messages =[
                {
                    "role": "user",
                    "content":[{"text":f"Write a 200-word blog about: {blogtopic}"}]
                }
            ],
            inferenceConfig={
                "maxTokens": max_tokens,
                "temperature": temperature,
                "topP": top_p
            }
        )

        text = response["output"]["message"]["content"][0]["text"]
        return text

    except Exception as e:
        print(f"Error generating Blog: {e}")
        return ""
def save_blog_details_s3(s3_key,s3_bucket,generate_blog):
    s3=boto3.client('s3')

    try:
        s3.put_object(Bucket=s3_bucket, Key=s3_key, Body=generate_blog)
        print("Code saved to s3")

    except Exception as e:
        print(f"Error when saving the code to s3. Details: {e}")

def lambda_handler(event, context):
    event=json.loads(event['body'])
    blogtopic=event['blog_topic']

    generate_blog=blog_generate(blogtopic=blogtopic)

    if generate_blog:
        current_time= datetime.now().strftime("%H%M%S")
        s3_key= f"blog-output/{current_time}.txt"
        s3_bucket="aws-bedrock-tut"
        save_blog_details_s3(s3_key,s3_bucket,generate_blog)
    
    else:
        print("No blog was generated")

    return{
        "statusCode":200,
        "body":json.dumps("Blog generation completed")
        
    }



