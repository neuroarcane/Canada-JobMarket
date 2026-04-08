import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import random

# Page config
st.set_page_config(
    page_title="Canada Job Market Analysis",
    page_icon="🍁",
    layout="wide"
)

# Static fake data for dashboard
jobs_data = {
    'title': [
        'Data Analyst', 'Software Engineer', 'Product Manager', 'DevOps Engineer',
        'Data Scientist', 'Frontend Developer', 'Backend Developer', 'UX Designer',
        'Marketing Manager', 'Sales Representative', 'Accountant', 'HR Manager',
        'Registered Nurse', 'Financial Analyst', 'Project Manager', 'Quality Assurance',
        'Business Analyst', 'Network Engineer', 'Security Analyst', 'Cloud Architect'
    ],
    'company': [
        'Shopify', 'RBC', 'TD Bank', 'Scotiabank', 'OpenText', 'CGI', 'IBM Canada',
        'Amazon Canada', 'Google Canada', 'Microsoft Canada', 'Telus', 'Rogers',
        'Deloitte', 'KPMG', 'PWC', 'Accenture', 'Manulife', 'Sun Life', 'Bell', 'BMO'
    ],
    'city': [
        'Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Toronto', 'Vancouver', 'Toronto',
        'Montreal', 'Toronto', 'Vancouver', 'Calgary', 'Ottawa', 'Toronto', 'Montreal',
        'Vancouver', 'Calgary', 'Toronto', 'Ottawa', 'Montreal', 'Vancouver'
    ],
    'salary_min': [
        60000, 85000, 95000, 80000, 90000, 70000, 85000, 65000,
        75000, 55000, 58000, 70000, 65000, 72000, 80000, 62000,
        68000, 75000, 85000, 110000
    ],
    'salary_max': [
        80000, 120000, 130000, 110000, 130000, 95000, 115000, 90000,
        100000, 75000, 75000, 95000, 80000, 95000, 110000, 85000,
        92000, 105000, 115000, 150000
    ],
    'remote': [
        'Hybrid', 'On-site', 'Remote', 'Hybrid', 'Remote', 'Hybrid', 'On-site', 'Remote',
        'Hybrid', 'On-site', 'On-site', 'Hybrid', 'On-site', 'Hybrid', 'Remote', 'Hybrid',
        'Remote', 'On-site', 'Hybrid', 'Remote'
    ],
    'industry': [
        'Tech', 'Finance', 'Finance', 'Finance', 'Tech', 'Tech', 'Tech', 'Tech',
        'Marketing', 'Sales', 'Finance', 'HR', 'Healthcare', 'Finance', 'Tech', 'Tech',
        'Consulting', 'Tech', 'Tech', 'Tech'
    ],
    'experience': [
        '2-4 years', '3-5 years', '5+ years', '3-5 years', '4+ years', '1-3 years', '3-5 years', '2-4 years',
        '5+ years', '0-2 years', '2-4 years', '5+ years', '2+ years', '3-5 years', '5+ years', '2-4 years',
        '3-5 years', '5+ years', '4+ years', '7+ years'
    ]
}

df = pd.DataFrame(jobs_data)

# Fake data for ML tools
fake_skills = [
    "Python", "SQL", "JavaScript", "React", "Node.js", "AWS", "Docker", 
    "Kubernetes", "Machine Learning", "Data Analysis", "Communication",
    "Project Management", "Agile", "Git", "REST APIs", "PostgreSQL",
    "MongoDB", "Azure", "Tableau", "Power BI", "Excel", "Leadership"
]

fake_jobs = {
    "Data Analyst": {
        "skills": ["Python", "SQL", "Tableau", "Excel", "Data Analysis"],
        "salary_range": "$65,000 - $85,000",
    },
    "Software Engineer": {
        "skills": ["Python", "JavaScript", "React", "Node.js", "Git", "AWS"],
        "salary_range": "$85,000 - $120,000",
    },
    "DevOps Engineer": {
        "skills": ["Docker", "Kubernetes", "AWS", "Python", "Git", "Linux"],
        "salary_range": "$90,000 - $130,000",
    },
    "Product Manager": {
        "skills": ["Project Management", "Agile", "Communication", "Leadership", "SQL"],
        "salary_range": "$95,000 - $140,000",
    },
    "Data Scientist": {
        "skills": ["Python", "Machine Learning", "SQL", "Statistics", "Data Analysis"],
        "salary_range": "$90,000 - $135,000",
    }
}

# Header
st.title("🍁 Canada Job Market Analysis")
st.markdown("### Complete Demo Platform - Dashboard + ML Tools")

# Warning banner
st.warning("⚠️ **DEMO MODE**: Using sample data for demonstration. Real data collection in progress!")

st.markdown("---")

# Main navigation
page = st.sidebar.radio(
    "Navigation",
    ["📊 Dashboard", "🤖 ML Tools", "ℹ️ About"]
)

# ========== DASHBOARD PAGE ==========
if page == "📊 Dashboard":
    
    # Key metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Jobs Tracked", "20", delta="Demo data")
    with col2:
        avg_salary = df[['salary_min', 'salary_max']].mean().mean()
        st.metric("Avg Salary", f"${avg_salary:,.0f}", delta="+12%")
    with col3:
        st.metric("Cities Covered", df['city'].nunique())
    with col4:
        remote_pct = (df['remote'] == 'Remote').sum() / len(df) * 100
        st.metric("Remote Jobs", f"{remote_pct:.0f}%")
    
    st.markdown("---")
    
    # Sidebar filters
    st.sidebar.header("Filters")
    selected_city = st.sidebar.multiselect(
        "Select Cities",
        options=df['city'].unique(),
        default=df['city'].unique()
    )
    
    selected_industry = st.sidebar.multiselect(
        "Select Industries",
        options=df['industry'].unique(),
        default=df['industry'].unique()
    )
    
    selected_remote = st.sidebar.multiselect(
        "Work Type",
        options=df['remote'].unique(),
        default=df['remote'].unique()
    )
    
    # Filter data
    filtered_df = df[
        (df['city'].isin(selected_city)) &
        (df['industry'].isin(selected_industry)) &
        (df['remote'].isin(selected_remote))
    ]
    
    # Dashboard tabs
    tab1, tab2, tab3 = st.tabs(["📈 Overview", "🗺️ Geographic", "💰 Salaries"])
    
    with tab1:
        st.subheader("Market Overview")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Jobs by city
            city_counts = filtered_df['city'].value_counts().reset_index()
            city_counts.columns = ['City', 'Count']
            fig1 = px.bar(
                city_counts,
                x='City',
                y='Count',
                title='Jobs by City',
                color='Count',
                color_continuous_scale='Blues'
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        with col2:
            # Jobs by industry
            industry_counts = filtered_df['industry'].value_counts().reset_index()
            industry_counts.columns = ['Industry', 'Count']
            fig2 = px.pie(
                industry_counts,
                values='Count',
                names='Industry',
                title='Jobs by Industry'
            )
            st.plotly_chart(fig2, use_container_width=True)
    
    with tab2:
        st.subheader("Geographic Distribution")
        
        city_stats = filtered_df.groupby('city').agg({
            'title': 'count',
            'salary_min': 'mean',
            'salary_max': 'mean'
        }).reset_index()
        city_stats.columns = ['City', 'Job Count', 'Avg Min Salary', 'Avg Max Salary']
        city_stats['Avg Salary'] = (city_stats['Avg Min Salary'] + city_stats['Avg Max Salary']) / 2
        
        fig3 = px.bar(
            city_stats,
            x='City',
            y='Job Count',
            title='Job Distribution Across Canadian Cities',
            color='Avg Salary',
            color_continuous_scale='RdYlGn',
            text='Job Count'
        )
        st.plotly_chart(fig3, use_container_width=True)
    
    with tab3:
        st.subheader("Salary Analysis")
        
        filtered_df['avg_salary'] = (filtered_df['salary_min'] + filtered_df['salary_max']) / 2
        
        col1, col2 = st.columns(2)
        
        with col1:
            salary_by_city = filtered_df.groupby('city')['avg_salary'].mean().reset_index()
            salary_by_city.columns = ['City', 'Average Salary']
            fig4 = px.bar(
                salary_by_city.sort_values('Average Salary', ascending=False),
                x='City',
                y='Average Salary',
                title='Average Salary by City',
                color='Average Salary',
                color_continuous_scale='Viridis'
            )
            st.plotly_chart(fig4, use_container_width=True)
        
        with col2:
            salary_by_industry = filtered_df.groupby('industry')['avg_salary'].mean().reset_index()
            salary_by_industry.columns = ['Industry', 'Average Salary']
            fig5 = px.bar(
                salary_by_industry.sort_values('Average Salary', ascending=False),
                x='Industry',
                y='Average Salary',
                title='Average Salary by Industry',
                color='Average Salary',
                color_continuous_scale='Plasma'
            )
            st.plotly_chart(fig5, use_container_width=True)

# ========== ML TOOLS PAGE ==========
elif page == "🤖 ML Tools":
    st.header("Interactive ML Tools")
    st.info("These tools demonstrate planned ML functionality using sample data")
    
    tool_tab = st.tabs(["📝 Job Analyzer", "🎯 Skills Matcher", "🗺️ Location Finder"])
    
    # Tool 1: Job Description Analyzer
    with tool_tab[0]:
        st.subheader("Job Description Analyzer")
        st.markdown("Paste a job description to extract skills and requirements")
        
        job_desc = st.text_area(
            "Job Description",
            placeholder="Paste job description here...",
            height=200
        )
        
        if st.button("Analyze Job Description", type="primary"):
            if job_desc and len(job_desc) > 20:
                # Fake extraction
                detected_skills = []
                for skill in fake_skills:
                    if skill.lower() in job_desc.lower():
                        detected_skills.append(skill)
                
                if not detected_skills:
                    detected_skills = random.sample(fake_skills, 5)
                
                # Experience detection
                if "senior" in job_desc.lower() or "lead" in job_desc.lower():
                    experience = "5+ years"
                elif "junior" in job_desc.lower() or "entry" in job_desc.lower():
                    experience = "0-2 years"
                else:
                    experience = "2-4 years"
                
                # Salary prediction
                salary_ranges = ["$60,000 - $80,000", "$70,000 - $95,000", "$85,000 - $120,000", "$90,000 - $130,000"]
                predicted_salary = random.choice(salary_ranges)
                
                # Display results
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Skills Detected", len(detected_skills))
                with col2:
                    st.metric("Experience Level", experience)
                with col3:
                    st.metric("Predicted Salary", predicted_salary)
                
                st.markdown("### Detected Skills")
                st.write(", ".join(detected_skills))
                
                st.success("Analysis complete! (Demo output)")
            else:
                st.error("Please enter a job description (at least 20 characters)")
    
    # Tool 2: Skills Matcher
    with tool_tab[1]:
        st.subheader("Skills Match Calculator")
        st.markdown("Enter your skills to find matching roles")
        
        user_skills = st.text_input(
            "Your Skills (comma-separated)",
            placeholder="e.g., Python, SQL, Machine Learning, Tableau"
        )
        
        if st.button("Find Matching Jobs", type="primary"):
            if user_skills and len(user_skills) > 3:
                skills_list = [s.strip() for s in user_skills.split(",")]
                
                # Calculate matches
                matches = []
                for job_title, job_info in fake_jobs.items():
                    required_skills = job_info["skills"]
                    matched = set(skills_list) & set(required_skills)
                    match_score = (len(matched) / len(required_skills)) * 100
                    
                    matches.append({
                        "job": job_title,
                        "score": match_score,
                        "matched_skills": list(matched),
                        "missing_skills": list(set(required_skills) - set(skills_list)),
                        "salary": job_info["salary_range"]
                    })
                
                matches.sort(key=lambda x: x["score"], reverse=True)
                
                st.markdown("### Your Best Matches")
                
                for idx, match in enumerate(matches[:5], 1):
                    with st.expander(f"{idx}. {match['job']} - {match['score']:.0f}% Match"):
                        st.write(f"**Salary Range:** {match['salary']}")
                        
                        if match['matched_skills']:
                            st.write(f"**✅ Your matching skills:** {', '.join(match['matched_skills'])}")
                        
                        if match['missing_skills']:
                            st.write(f"**📚 Skills to learn:** {', '.join(match['missing_skills'])}")
            else:
                st.error("Please enter your skills")
    
    # Tool 3: Location Recommender
    with tool_tab[2]:
        st.subheader("Location Recommender")
        st.markdown("Find the best Canadian city for your role")
        
        job_role = st.text_input("Job Role", placeholder="e.g., Software Engineer, Data Analyst")
        
        if st.button("Get City Recommendations", type="primary"):
            if job_role:
                # Fake city data
                cities = {
                    "Toronto": {"jobs": 120, "salary": 105000, "cost": "High"},
                    "Vancouver": {"jobs": 85, "salary": 98000, "cost": "Very High"},
                    "Montreal": {"jobs": 65, "salary": 82000, "cost": "Moderate"},
                    "Calgary": {"jobs": 45, "salary": 92000, "cost": "Moderate"},
                    "Ottawa": {"jobs": 55, "salary": 88000, "cost": "Moderate"}
                }
                
                st.markdown("### City Rankings")
                
                ranked = sorted(cities.items(), key=lambda x: x[1]["jobs"], reverse=True)
                
                for idx, (city, data) in enumerate(ranked, 1):
                    with st.expander(f"{idx}. {city}"):
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Job Openings", f"~{data['jobs']}")
                        with col2:
                            st.metric("Avg Salary", f"${data['salary']:,}")
                        with col3:
                            st.metric("Cost of Living", data['cost'])
                
                st.success(f"Top recommendation for {job_role}: {ranked[0][0]}")
            else:
                st.error("Please enter a job role")

# ========== ABOUT PAGE ==========
elif page == "ℹ️ About":
    st.header("About This Project")
    
    st.markdown("""
    ## 🍁 Canada Job Market Analysis
    
    ### What We're Building
    
    We're tracking Canada's job market for a month to understand what's actually happening - 
    what skills employers want, where the jobs are, salary ranges, and how the market evolves day-to-day.
    
    ### The Plan
    
    **Phase 1: Data Collection (30 days)**
    - Daily scraping of major Canadian job boards
    - Tracking company career pages
    - Building a comprehensive dataset
    
    **Phase 2: Analysis**
    - Skills demand analysis
    - Geographic patterns
    - Salary trends
    - Remote work insights
    - Industry comparisons
    
    ### Tech Stack
    
    - **Data Collection:** Python (BeautifulSoup, Selenium, Scrapy)
    - **Storage:** PostgreSQL / SQLite
    - **Processing:** Pandas, NumPy, spaCy
    - **Analysis:** Jupyter, scikit-learn
    - **Visualization:** Plotly, Matplotlib
    - **Apps:** Streamlit + Gradio (this demo!)
    - **Deployment:** Streamlit Cloud, Hugging Face Spaces
    
    ### Data Sources
    
    - Indeed Canada
    - LinkedIn
    - Workopolis
    - Government of Canada Job Bank
    - Company career pages (Shopify, RBC, TD, etc.)
    
    ### Current Status
    
    **Right now:** Planning and building data collection pipeline
    
    **Coming soon:** 30-day monitoring, analysis, real ML models
    
    ### Repository
    
    [github.com/neuroarcane/Canada-JobMarket](https://github.com/neuroarcane/Canada-JobMarket)
    
    ---
    
    **Note:** This is a demo using sample data. Real functionality will be powered by actual job market data.
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p style='font-size: 0.9em;'>🍁 Canada Job Market Analysis - Combined Demo Platform</p>
    <p style='font-size: 0.8em; color: gray;'>Dashboard + ML Tools | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
