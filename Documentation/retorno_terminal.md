(docetl) ➜ DocETL docetl run pipeline.yaml
[20:24:47] Checking operations...

           ✓ Operation 'summarize_by_topic' (reduce)
           ✓ Operation 'scan_law_analysis_step' (scan)

           ✓ Operation 'analyze_article' (map)
           ✓ Operation 'split_law_by_article' (split)
           ✓ Operation 'scan_lgpd_dataset' (scan)
           ✓ All operations passed syntax check

           Pipeline Steps:
           ■ law_analysis_step
           ■ topic_summary_step
           ╭─────────────────────────────────────────── Query Plan ───────────────────────────────────────────╮
           │ topic_summary_step/summarize_by_topic                                                            │
           │ Type: reduce                                                                                     │
           │ Output Schema:                                                                                   │
           │   topic_summary: string                                                                          │
           │ ▼                                                                                                │
           │   topic_summary_step/scan_law_analysis_step                                                      │
           │   Type: scan                                                                                     │
           │   ▼                                                                                              │
           │     law_analysis_step/analyze_article                                                            │
           │     Type: map                                                                                    │
           │     Output Schema:                                                                               │
           │       topic: string                                                                              │
           │       summary: string                                                                            │
           │     ▼                                                                                            │
           │       law_analysis_step/split_law_by_article                                                     │
           │       Type: split                                                                                │
           │       ▼                                                                                          │
           │         law_analysis_step/scan_lgpd_dataset                                                      │
           │         Type: scan                                                                               │
           ╰──────────────────────────────────────────────────────────────────────────────────────────────────╯


─────────────────────────────────────────────────────────────────────────────────────────────────── Loading Datasets ───────────────────────────────────────────────────────────────────────────────────────────────────
✓ Loaded dataset 'lgpd_dataset' from lgpd_dataset.json

────────────────────────────────────────────────────────────────────────────────────────────────── Pipeline Execution ──────────────────────────────────────────────────────────────────────────────────────────────────
✓ Loaded checkpoint for operation 'analyze_article' in step 'law_analysis_step' from intermediate_results/law_analysis_step/analyze_article.json  
 Flushing cache to disk...  
 Cache flushed to disk.  
 ╭────── Step Execution: law_analysis_step/boundary ──────╮  
 │ ✓ Using cached law_analysis_step/analyze_article │  
 │ Step law_analysis_step/boundary completed. Cost: $0.00 │  
 ╰────────────────────────────────────────────────────────╯  
 ✓ topic_summary_step/scan_law_analysis_step (Cost: $0.00)  
Processing summarize_by_topic (reduce) on all documents: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 36/36 [00:07<00:00, 4.83it/s]
[20:24:54] ✓ topic_summary_step/summarize_by_topic (Cost: $0.00)  
 ✓ Intermediate saved for operation 'summarize_by_topic' in step 'topic_summary_step' at intermediate_results/topic_summary_step/summarize_by_topic.json  
 Flushing cache to disk...  
 Cache flushed to disk.  
 ╭─────── Step Execution: topic_summary_step/boundary ───────╮  
 │ ✓ topic_summary_step/scan_law_analysis_step (Cost: $0.00) │  
 │ ✓ topic_summary_step/summarize_by_topic (Cost: $0.00) │  
 │ Step topic_summary_step/boundary completed. Cost: $0.00 │  
 ╰───────────────────────────────────────────────────────────╯  
 ✓ Saved to lgpd_summary_by_topic.json

           ╭──────────────────────────────────────────────────────────────────────────────────────────── Execution Summary ────────────────────────────────────────────────────────────────────────────────────────────╮
           │ Cost: $0.00                                                                                                                                                                                               │
           │ Time: 7.56s                                                                                                                                                                                               │
           │ Cache: intermediate_results                                                                                                                                                                               │
           │ Output: lgpd_summary_by_topic.json                                                                                                                                                                        │
           ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
