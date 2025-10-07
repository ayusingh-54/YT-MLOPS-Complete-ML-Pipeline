```mermaid
flowchart TD
	node1["data_ingestion"]
	node2["data_preprocessing"]
	node3["feature_engineering"]
	node4["model_building"]
	node5["model_evaluation"]
	node1-->node2
	node2-->node3
	node3-->node4
	node3-->node5
	node4-->node5
```