# PROXI: Challenging GNNs for Link Prediction

## Abstract
Over the past decade, Graph Neural Networks (GNNs) have transformed graph representation learning. In the widely adopted message-passing GNN framework, nodes refine their representations by aggregating information from neighboring nodes iteratively. While GNNs excel in various domains, recent theoretical studies have raised concerns about their capabilities. GNNs aim to address various graph-related tasks by utilizing such node representations; however, this one-size-fits-all approach proves suboptimal for diverse tasks.

Motivated by these observations, we conduct empirical tests to compare the performance of current GNN models with more conventional and direct methods in link prediction tasks. Introducing our model, PROXI, which leverages proximity information of node pairs in both graph and attribute spaces, we find that standard machine learning (ML) models perform competitively, even outperforming cutting-edge GNN models when applied to these proximity metrics derived from node neighborhoods and attributes. This holds true across both homophilic and heterophilic networks, as well as small and large benchmark datasets, including those from the Open Graph Benchmark (OGB). Moreover, we show that augmenting traditional GNNs with PROXI significantly boosts their link prediction performance. Our empirical findings corroborate the previously mentioned theoretical observations and imply that there exists ample room for enhancement in current GNN models to reach their potential.

## Overview
This repository contains the code implementation for generating feature vectors used in link prediction tasks, specifically designed to evaluate the effectiveness of PROXI against traditional GNN models.

### Features
- **Feature Vector Generation**: Implementations for generating feature vectors using the PROXI method.
- **Compatibility**: Works with various datasets, including Cora, Citeseer, Pubmed, Photo, Computers, Texas, Wisconsin, Chameleon, Squirrel, Crocodile, and OGBL-PPA.
- **Optimized for Link Prediction**: Empirical testing of the PROXI model against state-of-the-art GNNs and standard ML models.

## Repository Structure
- **General**: The codes in the `General` folder are tailored for processing datasets such as Cora, Citeseer, Pubmed, and more. They provide a generalized approach for generating feature vectors applicable across different domains.
- **Collab**: The codes in the `Collab` folder are specifically designed for the `ogbl-collab` dataset.
  
## Installation
To get started with PROXI, clone this repository and install the necessary dependencies:

```bash
git clone https://github.com/workrep20232/proxi.git

