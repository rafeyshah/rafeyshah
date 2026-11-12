<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/rafeyshah/rafeyshah/raw/main/assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/rafeyshah/rafeyshah/raw/main/assets/header-light.svg">
  <img src="https://github.com/rafeyshah/rafeyshah/raw/main/assets/header-dark.svg" width="100%" alt="Abdul Rafey — Full-Stack Engineer · MSc Data Science @ FAU · Open to work, Nuremberg">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/YOUR-LINKEDIN/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
  <a href="mailto:dev.abdulrafey@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"/></a>
  <img src="https://img.shields.io/badge/Nuremberg,%20Germany-30363D?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Nuremberg, Germany"/>
</p>

<p align="center">
  Full-Stack Engineer at <b>LeanoSol</b> and MSc Data Science student at <b>FAU Erlangen-Nürnberg</b>.<br/>
  I build web products that are tested, secure and deployed — and ML pipelines that are measured, not just trained.
</p>

<br/>

## ⭐ Featured — GawainBook

<a href="https://gawainbook.onrender.com">
  <img src="https://github.com/rafeyshah/GawainBook-SocialMediaApp/raw/master/docs/banner.svg" width="100%" alt="GawainBook banner"/>
</a>

**Reading circles without spoilers.** A full-stack TypeScript platform where small groups read the same book at their own pace — every discussion, reply, search result and notification stays locked until you reach that chapter.

<p>
  <a href="https://gawainbook.onrender.com"><img src="https://img.shields.io/badge/Live_demo-gawainbook.onrender.com-2EA44F?style=for-the-badge&logo=render&logoColor=white" alt="Live demo"/></a>
  <a href="https://github.com/rafeyshah/GawainBook-SocialMediaApp"><img src="https://img.shields.io/badge/Source_code-181717?style=for-the-badge&logo=github&logoColor=white" alt="Source code"/></a>
</p>

<table>
  <tr>
    <td width="50%" valign="top">

**What it does**
- Public and invite-only **reading circles** with organiser & moderator roles
- **Spoiler-locked discussions** + a "who's where" progress view
- **Library** with shelves, chapter-by-chapter progress and Open Library search
- **Social feed** — photo posts, spoiler covers, comments, likes, follows
- **Safety** — reporting, blocking, admin moderation, rate limits

</td>
    <td width="50%" valign="top">

**How it's built**
- One central **access policy**, also enforced in SQL — locked content never leaves the database
- Session cookies (hashed tokens), **CSRF protection**, bcrypt, Helmet
- Private S3-compatible photo storage with **presigned URLs**
- **1,100+ automated tests** — 661 API, 468 UI, Playwright E2E journeys
- CI on GitHub Actions, auto-deploy to **Render**

</td>
  </tr>
</table>

<p>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript"/>
  <img src="https://img.shields.io/badge/React-20232A?style=flat-square&logo=react&logoColor=61DAFB" alt="React"/>
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js"/>
  <img src="https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white" alt="Express"/>
  <img src="https://img.shields.io/badge/PostgreSQL_(Neon)-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/Drizzle_ORM-C5F74F?style=flat-square&logo=drizzle&logoColor=black" alt="Drizzle ORM"/>
  <img src="https://img.shields.io/badge/Jest-C21325?style=flat-square&logo=jest&logoColor=white" alt="Jest"/>
  <img src="https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white" alt="Playwright"/>
  <img src="https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=black" alt="Render"/>
</p>

<table>
  <tr>
    <td width="40%"><img src="https://github.com/rafeyshah/GawainBook-SocialMediaApp/raw/master/docs/screenshots/circle.png" alt="Reading circle with progress and locked discussions"/></td>
    <td width="40%"><img src="https://github.com/rafeyshah/GawainBook-SocialMediaApp/raw/master/docs/screenshots/discussion.png" alt="Chapter discussion"/></td>
    <td width="20%"><img src="https://github.com/rafeyshah/GawainBook-SocialMediaApp/raw/master/docs/screenshots/mobile-circle.png" alt="Mobile view"/></td>
  </tr>
  <tr>
    <td align="center"><sub>Reading circle · locked chapters</sub></td>
    <td align="center"><sub>Chapter discussion</sub></td>
    <td align="center"><sub>Mobile</sub></td>
  </tr>
</table>

<br/>

## 🔬 Research — GothiRead

**OCR & font recognition for historical Gothic scripts** · FAU Pattern Recognition Lab  
An end-to-end pipeline that transcribes multi-font historical documents *and* predicts the font group of every character — from dataset validation and grapheme-level normalisation to benchmarking, fine-tuning and ensembling.

| Task | Approach | Result |
|---|---|---|
| Text recognition | Fine-tuned PaddleOCR (benchmarked vs. TrOCR, Donut, PARSeq, ABINet) | **1.3% CER** · 8.0% WER |
| Font-group recognition | CRNN + Transformer (CTC) with risk-based ensemble | **2.1% font CER** on 17.9k lines |

<p>
  <a href="https://github.com/rafeyshah/gothi-read"><img src="https://img.shields.io/badge/Source_code-181717?style=flat-square&logo=github&logoColor=white" alt="Source code"/></a>
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black" alt="Hugging Face"/>
  <img src="https://img.shields.io/badge/PaddleOCR-0062B0?style=flat-square" alt="PaddleOCR"/>
  <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" alt="CUDA"/>
</p>

<br/>

## 🧩 More projects

| Project | Description | Stack |
|---|---|---|
| **[NASA-404](https://github.com/rafeyshah/NASA-404)** | Mission-control REST API with versioning, CSV ingestion, Node clustering and Jest/Supertest tests | Node.js · Express · MongoDB |
| **[VocareWebApp](https://github.com/rafeyshah/VocareWebApp)** | Calendar-based appointment management system | TypeScript · React |
| **[DineRank](https://github.com/rafeyshah/DineRank-RestaurantRating)** | Restaurant-rating prediction across 4 markets — EDA, feature engineering, model comparison | Python · pandas · scikit-learn |

<br/>

## 🛠️ Toolbox

<table>
  <tr>
    <td align="center" width="25%"><b>Frontend</b><br/><br/><img src="https://skillicons.dev/icons?i=ts,js,react,html,css,materialui&perline=3" alt="Frontend"/></td>
    <td align="center" width="25%"><b>Backend</b><br/><br/><img src="https://skillicons.dev/icons?i=nodejs,express,postgres,mongodb&perline=2" alt="Backend"/></td>
    <td align="center" width="25%"><b>ML / Data</b><br/><br/><img src="https://skillicons.dev/icons?i=python,pytorch,sklearn&perline=3" alt="ML / Data"/></td>
    <td align="center" width="25%"><b>Testing & Ops</b><br/><br/><img src="https://skillicons.dev/icons?i=jest,githubactions,git,linux&perline=2" alt="Testing and Ops"/></td>
  </tr>
</table>

<br/>

## 👨‍💻 Experience

| | Role | Company |
|---|---|---|
| **Now** | Full-Stack Engineer | LeanoSol · Nuremberg |
| 2024 | Working Student — IT Support / SysAdmin | Refair IT · Nuremberg |
| 2023–24 | Software Engineer | Discretelogix · Islamabad |
| 2022 | Data Science Intern | IPRI · Islamabad |

🎯 **Open to:** Full-Stack / Software Engineering roles · Werkstudent (15–20 h/week) · Master's thesis in ML / Document AI  
🗣️ English (fluent) · German (learning, A2)

<br/>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=rafeyshah&theme=github-dark-blue&hide_border=true&background=0D1117" alt="GitHub contribution streak"/>
</p>
