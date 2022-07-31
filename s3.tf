resource "aws_s3_bucket" "image_storage_bucket" {
    bucket = "lab-lambda-talent-academy-buc"

    tags = {
        Name = "lab-lambda-talent-academy-buc"
        Environment = "Lab"
    }
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.image_storage_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.lambda_image_rekognition.arn
    events              = ["s3:ObjectCreated:*"]
    
  }

  depends_on = [aws_lambda_permission.allow_bucket]
}