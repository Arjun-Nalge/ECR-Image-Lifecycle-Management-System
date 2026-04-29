import boto3
import datetime

ecr = boto3.client('ecr')

# Config
DAYS_OLD = 30

def lambda_handler(event, context):
    now = datetime.datetime.now(datetime.timezone.utc)

    repositories = ecr.describe_repositories()['repositories']

    for repo in repositories:
        repo_name = repo['repositoryName']
        print(f"Checking repository: {repo_name}")

        images = ecr.describe_images(repositoryName=repo_name)['imageDetails']
        images_to_delete = []

        for image in images:
            pushed_at = image.get('imagePushedAt')
            image_tags = image.get('imageTags', [])

            if not pushed_at:
                continue

            age = (now - pushed_at).days

            # Condition:
            # 1. Untagged images
            # 2. Older than threshold
            if age > DAYS_OLD or not image_tags:
                images_to_delete.append({
                    'imageDigest': image['imageDigest']
                })

        if images_to_delete:
            print(f"Deleting {len(images_to_delete)} images from {repo_name}")

            # ECR allows max 100 images per request
            for i in range(0, len(images_to_delete), 100):
                batch = images_to_delete[i:i+100]

                ecr.batch_delete_image(
                    repositoryName=repo_name,
                    imageIds=batch
                )
        else:
            print(f"No images to delete in {repo_name}")

    return {
        "status": "completed"
    }
