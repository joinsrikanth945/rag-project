# Agentic RAG System on Azure Kubernetes Service

**Complete Implementation Guide for Production-Ready Deployment**

This is a comprehensive, production-grade implementation of a Retrieval-Augmented Generation (RAG) system with agent orchestration, deployable on Azure Kubernetes Service (AKS).

---

## 📋 What You Get

This package includes:

1. **Complete Source Code**
   - FastAPI REST API with RAG agent
   - Document processing pipeline (PDF, DOCX, Excel, Text)
   - Vector store integration (Azure Cognitive Search)
   - LLM integration (Azure OpenAI)
   - LangChain-based agent orchestration

2. **Kubernetes Configuration**
   - Production-ready manifests
   - Auto-scaling (HPA)
   - Health checks & probes
   - Ingress configuration
   - Resource management

3. **Docker Setup**
   - Optimized Dockerfile
   - Docker Compose for local development
   - Multi-profile support (Prometheus, Grafana, etc.)

4. **Comprehensive Guides**
   - Architecture documentation
   - Step-by-step deployment guide
   - Testing and validation procedures
   - Quick start guide

---

## 🚀 Quick Navigation

### For First-Time Users
Start here → **QUICK_START.md**
- 30-45 minute deployment
- Step-by-step instructions
- Common operations

### Complete Implementation Details
→ **RAG_AGENT_AZURE_K8S_GUIDE.md**
- Full architecture overview
- Complete source code
- Configuration management
- Kubernetes manifests
- Production setup

### Testing & Validation
→ **TESTING_DEPLOYMENT_GUIDE.md**
- Local testing procedures
- Azure deployment testing
- Load testing with Locust
- Production smoke tests
- Monitoring setup

### Local Development
→ **docker-compose.yml**
- Test locally before Azure deployment
- Multiple profiles (basic, with-postgres, with-chroma, with-monitoring)
- Includes Redis cache, PostgreSQL, Chroma, Prometheus, Grafana

---

## 📦 File Structure

```
.
├── README.md                                  # This file
├── QUICK_START.md                            # 30-minute deployment guide
├── RAG_AGENT_AZURE_K8S_GUIDE.md             # Complete implementation guide
├── TESTING_DEPLOYMENT_GUIDE.md              # Testing procedures
├── requirements.txt                          # Python dependencies
├── .env.example                              # Environment variables template
├── docker-compose.yml                        # Local development setup
├── Dockerfile                                # Container image
│
├── src/                                      # Application source code
│   ├── main.py                               # FastAPI application
│   ├── config.py                             # Configuration management
│   ├── agents/
│   │   ├── rag_agent.py                      # RAG agent implementation
│   │   └── tools.py                          # Agent tools
│   ├── document_processing/
│   │   ├── loaders.py                        # Document loaders
│   │   ├── chunking.py                       # Text chunking
│   │   └── parsers/
│   │       ├── pdf_parser.py
│   │       ├── docx_parser.py
│   │       ├── excel_parser.py
│   │       ├── text_parser.py
│   │       └── web_scraper.py
│   ├── vector_store/
│   │   ├── azure_search.py                   # Azure Cognitive Search
│   │   └── chroma_store.py                   # Chroma vector store
│   ├── embeddings/
│   │   ├── azure_embeddings.py               # Azure OpenAI embeddings
│   │   └── hf_embeddings.py                  # HuggingFace embeddings
│   ├── llm/
│   │   └── azure_llm.py                      # Azure OpenAI LLM
│   ├── models/
│   │   └── schemas.py                        # Pydantic models
│   └── utils/
│       ├── logger.py
│       └── helpers.py
│
├── kubernetes/                               # Kubernetes manifests
│   ├── namespace.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── hpa.yaml                              # Horizontal Pod Autoscaler
│   └── pdb.yaml                              # Pod Disruption Budget
│
├── docker/                                   # Docker configuration
│   ├── Dockerfile
│   └── .dockerignore
│
├── scripts/                                  # Deployment scripts
│   ├── setup_azure_services.sh              # Azure resource creation
│   ├── build_image.sh                       # Docker build & push
│   ├── deploy_to_aks.sh                     # Kubernetes deployment
│   ├── test_deployment.sh                   # Deployment testing
│   └── ...
│
└── tests/                                    # Test suite
    ├── test_api.py                          # API tests
    ├── test_document_processing.py          # Document processing tests
    ├── test_agents.py                       # Agent tests
    ├── test_integration.py                  # Integration tests
    ├── load_test.py                         # Locust load tests
    └── smoke_tests.py                       # Production smoke tests
```

---

## 🔧 System Architecture

```
CLIENT APPLICATIONS
        ↓
  LOAD BALANCER
        ↓
┌─────────────────────────────┐
│   KUBERNETES CLUSTER (AKS)  │
│  ┌─────────────────────────┐│
│  │  RAG AGENT SERVICE      ││
│  │  (FastAPI + LangChain)  ││
│  └─────────┬───────────────┘│
│            ↓                 │
│  ┌─────────────────────────┐│
│  │ DOCUMENT INGESTION      ││
│  │ • PDF/DOCX/Excel/Text  ││
│  │ • Web Scraping         ││
│  │ • Chunking (5 chunks)  ││
│  └─────────┬───────────────┘│
│            ↓                 │
│  ┌─────────────────────────┐│
│  │ VECTOR DATABASE         ││
│  │ (Azure Cognitive Search)││
│  └─────────┬───────────────┘│
│            ↓                 │
│  ┌─────────────────────────┐│
│  │ EMBEDDINGS & LLM        ││
│  │ (Azure OpenAI Services) ││
│  └─────────────────────────┘│
└─────────────────────────────┘
```

---

## 📊 Supported Document Types

| Type | Format | Parser | Status |
|------|--------|--------|--------|
| PDF | .pdf | PyPDF2/pdfplumber | ✓ Included |
| Word | .docx | python-docx | ✓ Included |
| Excel | .xlsx/.xls | openpyxl | ✓ Included |
| Text | .txt | Native Python | ✓ Included |
| Web | URL | BeautifulSoup | ✓ Included |

---

## 🛠️ Technology Stack

### Core
- **Framework**: FastAPI (async)
- **Agent Orchestration**: LangChain 0.1.x
- **Containerization**: Docker & Kubernetes
- **Cloud Platform**: Microsoft Azure

### LLM & Embeddings
- **LLM**: Azure OpenAI (GPT-4 Turbo / GPT-3.5-turbo)
- **Embeddings**: Azure OpenAI text-embedding-3-small
- **Alternative**: HuggingFace models (optional)

### Data & Search
- **Vector Store**: Azure Cognitive Search
- **Alternative**: Chroma (local testing)
- **Language**: Python 3.11+

### Kubernetes & Orchestration
- **Container Orchestration**: AKS
- **Ingress**: Nginx
- **Scaling**: Horizontal Pod Autoscaler (HPA)
- **Monitoring**: Prometheus + Azure Monitor

---

## 🚀 Deployment Paths

### Path 1: Quick Start (Recommended for First Deploy)
1. Azure resource setup (10 min)
2. Local testing with Docker Compose (5 min)
3. Build Docker image (5 min)
4. Deploy to AKS (5 min)
5. Test deployment (5 min)
**Total: ~30-45 minutes**

See: **QUICK_START.md**

### Path 2: Full Production Setup
1. Detailed architecture review
2. Security hardening
3. Monitoring & logging setup
4. Load testing & optimization
5. Backup & disaster recovery
**Total: ~2-3 hours**

See: **RAG_AGENT_AZURE_K8S_GUIDE.md**

### Path 3: Local Development First
1. Clone/setup project
2. Create .env file
3. Run docker-compose
4. Test API locally
5. Run unit tests
6. Deploy to Azure

See: **docker-compose.yml** and **TESTING_DEPLOYMENT_GUIDE.md**

---

## 📋 Prerequisites

### Required
- Azure subscription (free trial works)
- Azure CLI: `az --version`
- kubectl: `kubectl version --client`
- Docker: `docker --version`
- Python 3.11+

### Azure Services Needed
- Azure OpenAI (GPT-4 Turbo deployment)
- Azure Cognitive Search
- Azure Kubernetes Service (AKS)
- Azure Storage Account
- Azure Container Registry (optional but recommended)

---

## ⚡ Quick Start (TL;DR)

```bash
# 1. Login to Azure
az login

# 2. Create resource group
az group create --name rag-rg --location eastus

# 3. Setup Azure services (see QUICK_START.md for full commands)
# This includes: ACR, AKS, Cognitive Search, Storage

# 4. Build and push Docker image
docker build -t ragazureacr.azurecr.io/rag-agent:latest .
az acr login --name ragazureacr
docker push ragazureacr.azurecr.io/rag-agent:latest

# 5. Deploy to Kubernetes
az aks get-credentials --resource-group rag-rg --name rag-aks
kubectl apply -f kubernetes/

# 6. Test
kubectl get svc -n rag-system  # Get external IP
curl http://<external-ip>/health
```

**For detailed steps**, see **QUICK_START.md**

---

## 🧪 Testing

### Local Testing
```bash
# Setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Test configuration
python test_config.py

# Test Azure connections
python test_azure_connections.py

# Run unit tests
pytest tests/ -v

# Run FastAPI server
python -m uvicorn src.main:app --reload

# In another terminal, test API
curl http://localhost:8000/health
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is this?"}'
```

### Docker Compose Local Testing
```bash
docker-compose up -d
curl http://localhost:8000/health
docker-compose logs -f rag-api
docker-compose down
```

### Azure Deployment Testing
```bash
# Port forward to local
kubectl port-forward svc/rag-agent-service 8000:80 -n rag-system

# Run smoke tests
python tests/smoke_tests.py

# Load testing
locust -f tests/load_test.py --host=http://localhost:8000 --users=100
```

For comprehensive testing procedures, see **TESTING_DEPLOYMENT_GUIDE.md**

---

## 📈 Performance Metrics

### Expected Performance
| Metric | Value | Notes |
|--------|-------|-------|
| Response Time (p99) | < 30s | Includes LLM inference |
| Vector Search Time | 50-200ms | Depends on corpus size |
| Throughput | 100+ req/s | With auto-scaling |
| Availability | > 99.5% | With 3+ replicas |
| Cold Start | 40s | Initial container startup |

### Scaling Configuration
- **Min Replicas**: 3
- **Max Replicas**: 10
- **CPU Target**: 70%
- **Memory Target**: 80%
- **Scale-up Time**: 30-60s
- **Scale-down Time**: 5 minutes

---

## 💰 Cost Estimation

### Monthly Costs (Minimal Setup)
| Service | Cost | Notes |
|---------|------|-------|
| AKS Cluster | $180 | 3x D2s_v3 nodes |
| Azure OpenAI | $50+ | Usage-based |
| Cognitive Search | $40 | Basic tier |
| Storage | $10 | Blob storage |
| Data Transfer | $5 | ~1GB |
| **Total** | **~$285** | Can scale up/down |

### Cost Optimization Tips
- Use spot instances for non-critical workloads
- Scale down cluster during off-hours
- Optimize chunk size to reduce API calls
- Cache embeddings where possible
- Use GPT-3.5-turbo instead of GPT-4 if acceptable

---

## 🔒 Security Considerations

### Implemented
- ✓ Azure Key Vault integration (recommended)
- ✓ Service account RBAC
- ✓ Resource quotas & limits
- ✓ Network policies (can be enabled)
- ✓ Health checks & auto-recovery

### Recommended for Production
- [ ] Enable Azure AD authentication
- [ ] Setup HTTPS/TLS certificates
- [ ] Implement request rate limiting
- [ ] Add API key authentication
- [ ] Enable audit logging
- [ ] Setup DDoS protection
- [ ] Enable network policies
- [ ] Use Pod Security Policies

See security recommendations in **RAG_AGENT_AZURE_K8S_GUIDE.md**

---

## 📚 Document Processing Details

### Input Document Format
- **10 PDFs**: Multi-page documents with tables & graphics
- **20 Word Docs**: .docx files with formatting
- **20 Excel Files**: .xlsx with multiple sheets
- **40 Text Files**: .txt with various encodings
- **1 Intranet URL**: Web content scraping

### Output Format (5 Chunks)
Each query returns up to 5 relevant document chunks:
```json
{
  "status": "success",
  "question": "What is the policy?",
  "answer": "Based on documents: [chunk1], [chunk2], ...",
  "chunks": [
    {
      "content": "...",
      "source": "document.pdf",
      "score": 0.95
    },
    // ... up to 5 chunks
  ]
}
```

### Chunking Strategy
- **Chunk Size**: 1000 characters (configurable)
- **Overlap**: 200 characters (configurable)
- **Separators**: "\n\n", "\n", ". ", " "
- **Purpose**: Balance between context and efficiency

---

## 🔄 Workflow

### Ingestion Pipeline
```
Documents → Parse → Chunk (1000 char) → Embed → Vector Store
```

### Query Pipeline
```
User Query → Embed → Vector Search (top 5) → LLM Agent → Response
```

### Agent Flow
1. User asks question
2. Agent retrieves context chunks via `retrieve_context` tool
3. Agent processes context with LLM
4. Agent returns formatted answer with sources

---

## 🛠️ Maintenance

### Regular Tasks
- Monitor pod resource usage
- Review application logs daily
- Check error rates and latency
- Validate auto-scaling behavior
- Test backup procedures
- Review and rotate secrets

### Updates
```bash
# Update Docker image
docker build -t ragazureacr.azurecr.io/rag-agent:v2 .
docker push ragazureacr.azurecr.io/rag-agent:v2

# Update deployment
kubectl set image deployment/rag-agent-api \
  rag-api=ragazureacr.azurecr.io/rag-agent:v2 -n rag-system

# Monitor rollout
kubectl rollout status deployment/rag-agent-api -n rag-system
```

### Rollback
```bash
kubectl rollout undo deployment/rag-agent-api -n rag-system
```

---

## 🐛 Troubleshooting

### Pod Not Starting
```bash
kubectl describe pod <pod-name> -n rag-system
kubectl logs <pod-name> -n rag-system
```

### Azure Connection Issues
```bash
# Test configuration
python -c "from src.config import settings; print(settings.AZURE_OPENAI_ENDPOINT)"

# Test connectivity
python test_azure_connections.py
```

### High Memory Usage
```bash
kubectl top pods -n rag-system --containers
# Reduce chunk size or add more replicas
```

### Slow Response Times
```bash
# Check vector search latency
# Check LLM API latency
# Monitor network bandwidth
# Review database indexes
```

See **TESTING_DEPLOYMENT_GUIDE.md** for detailed troubleshooting.

---

## 📖 Documentation Map

| Need | Document |
|------|----------|
| Get started in 30 minutes | **QUICK_START.md** |
| Understand complete architecture | **RAG_AGENT_AZURE_K8S_GUIDE.md** |
| Test and validate deployment | **TESTING_DEPLOYMENT_GUIDE.md** |
| Local development setup | **docker-compose.yml** |
| Environment configuration | **.env.example** |

---

## 🤝 Support

### Common Issues

**Q: Pods stuck in CrashLoopBackOff?**
- Check environment variables are set
- Verify Azure credentials
- Check container logs: `kubectl logs <pod-name> -n rag-system`

**Q: No external IP assigned?**
- Wait 1-2 minutes for LB provisioning
- Check service status: `kubectl describe svc rag-agent-service -n rag-system`

**Q: High costs?**
- Use Azure Cost Analysis
- Scale down during off-hours
- Consider spot instances
- Optimize chunk sizes

**Q: Vector search slow?**
- Increase Azure Cognitive Search SKU
- Check index size and metrics
- Consider batch queries

---

## ✨ Features

- ✓ Multi-format document support (PDF, DOCX, Excel, TXT)
- ✓ Web content ingestion
- ✓ Intelligent text chunking
- ✓ LangChain agent orchestration
- ✓ Azure OpenAI integration
- ✓ Vector search with top-5 retrieval
- ✓ Auto-scaling (HPA)
- ✓ Health checks & monitoring
- ✓ Production-ready Kubernetes manifests
- ✓ Comprehensive testing suite
- ✓ Docker & docker-compose support

---

## 📝 Notes

### Design Decisions
1. **LangChain over raw APIs**: Simplified agent management & tool use
2. **Azure Cognitive Search over in-memory**: Scalable, production-grade vector DB
3. **Top-5 chunks**: Balance between context and cost
4. **FastAPI over Flask**: Native async support, better performance
5. **AKS over manual VMs**: Automatic scaling, built-in monitoring

### Limitations
- Max chunk size: 1000 characters (configurable)
- Vector search: Azure Cognitive Search required
- LLM: Azure OpenAI required (can swap with other providers)
- Language: English-optimized (multilingual possible)

### Future Enhancements
- [ ] User authentication & API keys
- [ ] Query caching
- [ ] Feedback loop for model fine-tuning
- [ ] Multiple LLM provider support
- [ ] Streaming responses
- [ ] Query analytics dashboard
- [ ] Multi-language support
- [ ] Custom embedding models

---

## 📄 License

This project is provided as-is for educational and commercial use.

---

## 🎯 Summary

You now have a **complete, production-ready RAG system** with:

1. ✅ Full source code (Python/FastAPI)
2. ✅ Kubernetes manifests (ready for AKS)
3. ✅ Docker configuration (local testing)
4. ✅ Comprehensive documentation
5. ✅ Testing procedures
6. ✅ Deployment scripts
7. ✅ Performance optimization
8. ✅ Security best practices

**Start with**: `QUICK_START.md` for a 30-minute deployment
**Deep dive**: `RAG_AGENT_AZURE_K8S_GUIDE.md` for complete details

---

**Happy deploying! 🚀**
