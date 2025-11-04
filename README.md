# AWS
a serverless web application that does CRUD operation on data through an HTML form hosted on EC2, processes it via Lambda functions, and stores it in DynamoDB.

Architecture Components
EC2 Instance: Hosts a static HTML form API Gateway: REST API endpoint Lambda Functions: Process form data DynamoDB: Stores submitted form data IAM Roles: Secure permissions between services

Detailed Requirements
DynamoDB Table Design Create a table named UserSubmissions with: Partition Key: submissionId (String) Attributes: name, email, message, submissionDate, status
Lambda Functions Create two Lambda functions Submission Lambda: Triggered by API Gateway POST request Validates input data Generates unique submissionId Stores data in DynamoDB Returns success/error response Query Lambda: Triggered by API Gateway GET request Retrieves submissions from DynamoDB Supports querying by email or fetching all records
API Gateway REST API with two resources: POST /submit → Submission Lambda GET /submissions → Query Lambda Enable CORS for EC2 domain
EC2 Instance Launch t2.micro instance with Amazon Linux Install web server (Apache/Nginx) Host static HTML form with fields: Name (text, required) Email (email, required) Message (textarea, required) JavaScript to handle form submission to API Gateway
IAM Roles Lambda execution role with DynamoDB read/write permissions EC2 instance profile (if needed) Note: The HTML form should use CSS and Bootstrap.

DYNAMO-DB
<img width="1310" height="557" alt="image" src="https://github.com/user-attachments/assets/298fccd0-3b75-4207-8545-c288e7b8bbba" />
