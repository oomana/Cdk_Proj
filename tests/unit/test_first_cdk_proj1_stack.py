import aws_cdk as core
import aws_cdk.assertions as assertions

from first_cdk_proj1.first_cdk_proj1_stack import FirstCdkProj1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in first_cdk_proj1/first_cdk_proj1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = FirstCdkProj1Stack(app, "first-cdk-proj1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
