import os
from aws_cdk import (
    Stack,
    App,
    Duration,
    aws_cloudwatch as cloudwatch,
)
from constructs import Construct

IMAGE_TAG = os.environ.get("IMAGE_TAG", "0001")

class RdsDashboardStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        account = Stack.of(self).account
        region = Stack.of(self).region

        # Account mapping - update these with your actual account IDs
        accounts = {
            "Production": "813627167089",
            "QA": "417848721801",
            "Dev": "957939121582",
            "Staging": "048136415067"
        }
        
        # Create the RDS dashboard
        dashboard = cloudwatch.Dashboard(
            self, "RDS-All-Environments",
            dashboard_name="RDS-All-Environments",
        )
        
        # ===================================================================
        # SECTION 1: RESOURCE UTILIZATION
        # ===================================================================
        dashboard.add_widgets(
            cloudwatch.TextWidget(
                markdown="# Resource Utilization",
                width=24,
                height=1
            )
        )
        
        # CPU Utilization - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="CPU Utilization - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} CPUUtilization', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # CPU Utilization - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} CPUUtilization AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} CPUUtilization AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} CPUUtilization AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} CPUUtilization AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # Database Connections - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Database Connections - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} DatabaseConnections', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Database Connections - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} DatabaseConnections AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} DatabaseConnections AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} DatabaseConnections AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} DatabaseConnections AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # Freeable Memory - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Freeable Memory - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} FreeableMemory', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Freeable Memory - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} FreeableMemory AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} FreeableMemory AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} FreeableMemory AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} FreeableMemory AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # Free Storage Space - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Free Storage Space - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} FreeStorageSpace', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Free Storage Space - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} FreeStorageSpace AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} FreeStorageSpace AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} FreeStorageSpace AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} FreeStorageSpace AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # ===================================================================
        # SECTION 2: I/O PERFORMANCE
        # ===================================================================
        dashboard.add_widgets(
            cloudwatch.TextWidget(
                markdown="# I/O Performance",
                width=24,
                height=1
            )
        )
        
        # Read IOPS - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Read IOPS - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} ReadIOPS', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Read IOPS - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ReadIOPS AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ReadIOPS AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ReadIOPS AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ReadIOPS AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # Write IOPS - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Write IOPS - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} WriteIOPS', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Write IOPS - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} WriteIOPS AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} WriteIOPS AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} WriteIOPS AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} WriteIOPS AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # Read Latency - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Read Latency - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} ReadLatency', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Read Latency - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ReadLatency AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ReadLatency AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ReadLatency AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ReadLatency AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # Write Latency - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Write Latency - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} WriteLatency', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Write Latency - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} WriteLatency AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} WriteLatency AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} WriteLatency AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} WriteLatency AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Seconds"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # ===================================================================
        # SECTION 3: NETWORK THROUGHPUT
        # ===================================================================
        dashboard.add_widgets(
            cloudwatch.TextWidget(
                markdown="# Network Throughput",
                width=24,
                height=1
            )
        )
        
        # Network Receive Throughput - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Network Receive Throughput - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} NetworkReceiveThroughput', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Network Receive Throughput - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} NetworkReceiveThroughput AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} NetworkReceiveThroughput AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} NetworkReceiveThroughput AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} NetworkReceiveThroughput AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # Network Transmit Throughput - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Network Transmit Throughput - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} NetworkTransmitThroughput', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Network Transmit Throughput - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} NetworkTransmitThroughput AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} NetworkTransmitThroughput AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} NetworkTransmitThroughput AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} NetworkTransmitThroughput AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Bytes/Second"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # ===================================================================
        # SECTION 4: AURORA SERVERLESS V2 (Optional - comment out if not needed)
        # ===================================================================
        dashboard.add_widgets(
            cloudwatch.TextWidget(
                markdown="# Aurora Serverless v2 Metrics (if applicable)",
                width=24,
                height=1
            )
        )
        
        # ACU Utilization - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="ACU Utilization - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} ACUUtilization', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # ACU Utilization - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ACUUtilization AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ACUUtilization AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ACUUtilization AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ACUUtilization AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Percent"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )
        
        # Serverless Database Capacity - Overview
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Serverless Database Capacity (ACUs) - Environment Comparison",
                width=24,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression="SEARCH('{AWS/RDS,DBInstanceIdentifier} ServerlessDatabaseCapacity', 'Average') GROUP BY aws.AccountId",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.RIGHT,
            )
        )
        
        # Serverless Database Capacity - Detail per environment
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="Production",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ServerlessDatabaseCapacity AND aws.AccountId=\"{accounts['Production']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="QA",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ServerlessDatabaseCapacity AND aws.AccountId=\"{accounts['QA']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Dev",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ServerlessDatabaseCapacity AND aws.AccountId=\"{accounts['Dev']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            ),
            cloudwatch.GraphWidget(
                title="Staging",
                width=6,
                height=6,
                left=[
                    cloudwatch.MathExpression(
                        expression=f"SEARCH('{{AWS/RDS,DBInstanceIdentifier}} ServerlessDatabaseCapacity AND aws.AccountId=\"{accounts['Staging']}\"', 'Average')",
                        label="",
                        period=Duration.minutes(1),
                    )
                ],
                left_y_axis=cloudwatch.YAxisProps(label="Count"),
                legend_position=cloudwatch.LegendPosition.BOTTOM,
            )
        )


app = App()
RdsDashboardStack(app, "RdsDashboardStack")
app.synth()