# Capstone Project: Salary Prediction
by [*Kantaphon Vareekasem*](https://github.com/Tatadektep) 
[**LinkedIn**](https://www.linkedin.com/in/kantaphon-tata-vareekasem/)

“Learn how to set goals. That's the key to everything. That includes designing your own success. You define what the goal is, it's not somebody else's goal, it's yours.” - Drew Carey
In this project, we aim to develop an application that can help job seekers to compare salaries on different companies, locations and more.

### [Presentation Deck](https://docs.google.com/presentation/d/1wuFNchdLq1EmiAhgZ1OxkKycmU4Ak3TQaQiDFMkywWs/edit?usp=sharing)

## Contents:
- [Executive Summary](#Executive-Summary)
- [Problem Statement](#Problem-Statement)
- [Benefit to Business](#Benefit-to-Business)
- [Conclusions](#Conclusions)
- [Recommendations](#Recommendations)
- [Future Works](#Future-Works) 
- [Contributors](#Contributors)

## Executive summary:
Pay is one of the most important factors in considering a new job. Yet, only a small percentage of companies has explicitly state the salary range. The information asymetric could lead unoptimised outcome for job seeker as business have significant advanatges for the candidates. 

Salary prediction model are important tool used to help job seeker get more accurate salary depending on multiple factors. The goal of this project is to provide accurate salary guidance to increase pay transparency for new job seekers along with the best practices to improve necessary skills. A study from Glassdoor found that an average American's earning could be about $7,500 more per year. Furthermore, lower initial salary has compounding effects where it could affect subsequent salary offer. This could cost candidates over $600,000 over the course of the career.

The main assumption is that similarly skilled candidates should be able to negotiate with a comparable salary range. However, there are many factors outside the scope of this project which have considerable impact on the salary range such as years of experience, education level, personality, negotiation skills and personal beliefs. 

### Problem Statement
1. Salary range and salary data are rarely transparent for most companies. There are some public available salary for most large companies in the demanding industries such as technology industry. The lack of transparency can be major obstacles for inexperienced workers from students, graduates and career changers to switch into a different industries. Furthermore, this could unintentionally lead to discrimination and inequality issues due to systemic biases.
2. Many qualified candidates are hired below their job level. It is difficult to objectively evaluate your current salary and potential job offers compared to the job market especially for niche industry and/or company without considerable dataset or industry experts.
3. Understand the value of each skillset and to find possible career paths based on current position. Moreover, the job seeker can.

### Dataset
[Glassdoor Job Postings : Data Science USA 2020](https://www.kaggle.com/datasets/atharvap329/glassdoor-data-science-job-data)

The dataset is composed of a train and test folder, each with data roles and non-data roles. Within the dataset contains job postings scraped by using the keyword of 'Data Scientist' from glassdoor.com to analyzed the gathered data and predict accurate salary range. The dataset is collected from jobs in the USA in the 2020. After removing duplicated job posting and one without a salary range, the dataset contains a total of 1790 positions where 1137 positions relating to data positions and 653 positions that are unrelated to data positions. Most of the data gather from the following states: California, Washington, New York as major areas to find the data related roles.


### Benefit to Business
1. Candidates would be able to develop relevant skills to adequately fulfil the need of business especially for the labour shortage in the IT market sector.
2. Business would be able to employed larger number of workers with diverse skillset and perspective especially from disadvantaged segment group of workers at the competitive price.
3. The company can significantly improve employee retention and compete with larger companies by providing The cost of losing an employee to the competition due to outdated compensation can be directly or indirectly cost as much as 60 percent of former employee's annual salary and up to 200 percent according to the study by the Society for Human Resources Management (SHRM) .

### Conclusion
1. Salary prediction model performs better than the baseline model and publicly established salary range for some industries. However, the model error is quite significant at ~$24,750 or 30% due to the insufficient number of data and features explaining the salary. 
2. Lasso regression achieve the lowest error due to shrinkage of data values to the mean i.e. the penalities which zero of the coefficients of some categorical variables to encourage simple model with fewer parameters. Some locations and companies have high variance on salary but most have similar level to the mean.
3. There are considerable numbers of external factor outside of the model with significant effect on salary level mainly personality and negotiation skills.

### Key Findings
1. The salary prediction from job post provide similar range to salary survey. This support that salary surveys are reliable sources of information and should be fully explored if available.
2. The main factors affecting the minimum salary are location, company and job title but the magnitude of the effect depending on each position with considerable variance between them. 
3. There are considerable external factors outside of the features provided in this model to predict salary salary from the specific experience required, macroeconomic factors and urgency of need to fill the position.

### Recommendation
1. Market research: Extensive market research for the specific company, industry, and location 
It would be best to research the employer before applying for the job to ensure your goals and mission aligns with the target company, and to identify which companies are the best fit according to your area of interest, skills and, expertise.[Source](https://www.linkedin.com/pulse/why-company-research-important-tool-job-seekers-sahasha-namdeo/) 
2. Networking: 1. Focus on Learning: Mindset shift to see networking as an opportunity for discovery and learning rather than a chore. The conversation might brings up new ideas and leads to new experiences and opportunities.[Source](https://hbr.org/2016/05/learn-to-love-networking)
3. Get a career coach:  Career coaches provide a range of services, from helping you figure out what you want to do to exploring opportunities for professional growth to supporting you through the ups and downs of looking for a new job.[Source](https://hbr.org/2022/02/do-you-need-a-career-coach)

### Future Works 
- Extract More Data from different websites and country to understand the unique environment 
- Expand the dataset to include more positions especially niche roles
- Explore the variance of work relating to job titles and job description.
- Explore total compensation with bonus and non-cash compensation instead of the minimum base salary.

- Glassdoor Job Postings : Data Science Positions Thailand 2022 Using [Kevin Xuande: Glassdoor Scraper](https://github.com/kelvinxuande/glassdoor-scraper)

### References:
[Adecco Reveals Salary Rates and High-Demand Jobs in 2021](https://adecco.co.th/en/news/detail/salary-guide-2021)

[How to do Salary Research](https://www.youtube.com/watch?v=45c_2UE7ZKs)

[How To Get the Salary You Want: Twelve Negotiation Tactics That Work](https://www.brodow.com/how-to-get-the-salary-you-want-twelve-negotiation-tactics-that-work)

[JobsDB by SEEK Salary Report 2022](https://th.jobsdb.com/en-th/cms/employer/wp-content/themes/jobsdb/assets/pdf/TH-EN-SalaryReport-03FEB2022.pdf)

[Salary Negotiation: Top Mistakes to AVOID | Indeed Career Tips](https://www.youtube.com/watch?v=bx9bTbN5wH0)

[Salary Prediction in the IT Job Market with Few High-Dimensional Samples: A Spanish Case Study](https://www.researchgate.net/publication/327080220_Salary_Prediction_in_the_IT_Job_Market_with_Few_High-Dimensional_Samples_A_Spanish_Case_Study)

[SALARY PREDICTION USING MACHINE LEARNING](http://ijasret.com/VolumeArticles/FullTextPDF/842_47._SALARY_PREDICTION_USING_MACHINE_LEARNING.pdf)

[Tech Salary Trends](https://www.dice.com/technologists/ebooks/tech-salary-report/salary-trends/)

[Words Matter: The Text of Online Job Postings Can Predict Salaries](https://hai.stanford.edu/news/words-matter-text-online-job-postings-can-predict-salaries)

### Contributors:
Special thanks to all the contributors who have contributed to this project. We are heartily thankful to you all.

And a special thanks to the instructional teams: *James Larkin*, *Yamada Nozomi*, and *Apiwat Jaroonpol* for their support.
