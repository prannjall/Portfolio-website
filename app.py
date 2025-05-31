from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.urandom(24)

# Profile data
PROFILE_DATA = {
    'name': 'Pranjal Tripathi',
    'title': 'Product Manager Leader | Cloud Platforms, SaaS, AI/ML | Salesforce',
    'summary': '''Pranjal Tripathi is a seasoned product leader with over 12 years of experience driving innovation across enterprise SaaS, iPaaS, and cloud integration platforms. As a Director-level Product Manager at Salesforce, Pranjal leads product strategy, roadmap execution, and cross-functional alignment for high-scale platforms such as CloudHub and MuleSoft Runtime Engine. He combines deep technical acumen with a customer-first mindset to deliver products that drive revenue, efficiency, and user satisfaction. Pranjal has a consistent track record of launching transformative products and leading global product teams across the U.S. and India. His core strengths include enterprise product lifecycle ownership, stakeholder alignment, product-led growth strategies, and cross-functional team leadership. His leadership extends to driving complex migrations, AI/ML feature integration, and digital transformation across regulated industries such as mortgage, banking, and healthcare. Previously, he led product development at ServiceLink, increasing operational revenue by over $17M through strategic automation and SaaS platform innovation. He holds a Master's in Information Systems Management from Carnegie Mellon University and is a Microsoft Azure Certified professional. Pranjal is passionate about solving hard problems at scale and building high-performance product organizations.''',
    'experience': [
        {
            'title': 'Senior Product Manager - CloudHub',
            'company': 'Salesforce',
            'duration': 'Aug 2024 - Present',
            'location': 'Seattle, Washington, United States · Hybrid',
            'description': '''Lead product strategy and roadmap execution for CloudHub – MuleSoft's iPaaS platform – supporting global customers in hybrid and multi-cloud environments.

Defined the product vision and roadmap for CloudHub, including VPC, dedicated load balancers, and secure VPN connectivity.
Collaborated with engineering, UX, and go-to-market teams to drive end-to-end product delivery with a strong customer feedback loop.
Championed customer-centric design by proactively engaging with enterprise clients, capturing pain points, and incorporating insights into the roadmap.
Launched telemetry and usage tracking initiatives to monitor key KPIs including adoption, performance, and NPS.
Enabled enterprise-grade cloud deployments by integrating with AWS Transit Gateway, improving network control and scalability for large clients.
Provided leadership across cross-functional teams to ensure on-time releases and field enablement success.'''
        },
        {
            'title': 'Senior Product Manager - Mule Runtime, HTTP Connector & Mule SDK',
            'company': 'Salesforce',
            'duration': 'Mar 2023 - Present',
            'location': 'Seattle, Washington, United States · Remote',
            'description': '''Spearhead core platform capabilities including Mule Runtime, HTTP Connector, and Java/XML SDKs, powering thousands of mission-critical integrations.

Owned product lifecycle for HTTP connectors and Mule SDK, improving developer experience and reducing onboarding time.
Partnered with field engineering and support to close the loop on customer feedback and reduce support ticket volumes.
Delivered SDK improvements that reduced connector development time by 30% across partner ecosystem.
Defined success metrics for product health and stability, monitored usage trends, and iterated features to align with customer demand.
Contributed to long-term vision for extensibility and scalability of MuleSoft's core platform.'''
        },
        {
            'title': 'Senior Product Manager - DataWeave, Mule SDK, MMA & Mule 3.x EOL',
            'company': 'Salesforce',
            'duration': 'Sep 2022 - Apr 2023',
            'location': 'Pittsburgh, Pennsylvania, United States',
            'description': '''Led platform migration tools and transformation language efforts, enabling smooth transitions for customers and ensuring long-term product scalability.

Managed End-of-Life strategy for Mule 3.x, affecting over 1,000 enterprise applications globally.
Launched Mule Migration Assistant (MMA), reducing migration time by 40% for legacy applications.
Advanced DataWeave capabilities to handle increasingly complex enterprise transformations.
Aligned upgrade tooling with broader Salesforce platform initiatives to ensure consistency and security.'''
        },
        {
            'title': 'Senior Product Manager',
            'company': 'ServiceLink (Fidelity National Financial)',
            'duration': 'Jul 2020 – Feb 2022',
            'location': 'Pittsburgh, Pennsylvania, United States',
            'description': '''Directed digital transformation of mortgage SaaS platforms serving SMBs and consumers, driving revenue growth and operational scale.

Delivered $15M+ revenue impact by launching a digital onboarding and closing platform for borrowers and buyers.
Defined vision, roadmap, and OKRs for enterprise products used across all 50 U.S. states.
Mentored and led globally distributed teams through Agile/Scrum execution cycles, backlog grooming, and delivery milestones.
Introduced analytics-driven feature prioritization and dashboards to measure real-time performance.'''
        },
        {
            'title': 'Product Manager',
            'company': 'ServiceLink (Fidelity National Financial)',
            'duration': 'Dec 2017 – Jul 2020',
            'location': 'Pittsburgh, Pennsylvania, United States',
            'description': '''Launched 4 major products in 2 years, improving time-to-close by over 90% and increasing revenue by 40%.

Delivered API-based title commitment solutions integrated with mortgage data providers.
Led 4 product teams, improving cross-functional execution and UX design through direct customer engagement.
Integrated AI/ML techniques and NLP to enhance automation and document processing capabilities.
Conducted in-depth competitive analysis to identify differentiation opportunities and go-to-market positioning.'''
        },
        {
            'title': 'Product Management Consultant',
            'company': 'Deloitte',
            'duration': 'Jan 2017 – May 2017',
            'location': 'Pittsburgh, Pennsylvania, United States',
            'description': '''Delivered an end-to-end cognitive computing product in the healthcare domain for early-stage diabetes awareness.

Applied predictive analytics, data mining, and ML algorithms to forecast likelihood of diabetes occurrence in patients.
Designed and implemented a cloud-hosted solution using Python (Django) for the frontend and Microsoft Azure ML Studio for backend prediction.
Created compelling data visualizations and dashboards to communicate model accuracy and healthcare impact.
Drove rapid product iteration and prototyping within a 5-month cycle while collaborating with data scientists and stakeholders.'''
        },
        {
            'title': 'Senior Product Data Analyst – BestBuy (Retail Analytics)',
            'company': 'Tata Consultancy Services',
            'duration': 'Jun 2015 – Mar 2016',
            'location': 'Pune, India',
            'description': '''Led a 5-member team delivering retail analytics and automation strategies to support BestBuy's digital transformation.

Developed statistical models and predictive analytics to enable data-driven product decisions.
Automated Excel-based leadership reports, saving 2+ hours of daily manual effort.
Devised a strategic decommissioning plan for legacy systems based on business needs and cost insights.
Interfaced with senior client stakeholders, translated business requirements into product documentation, and validated end-to-end testing.
Conducted team mentoring, technical knowledge transfer, and peer training programs.'''
        },
        {
            'title': 'Product Data Analyst – MUFG Union Bank',
            'company': 'Tata Consultancy Services',
            'duration': 'Jun 2012 – May 2015',
            'location': 'Pune, India',
            'description': '''Delivered data analytics and platform improvement solutions for one of the largest Japanese banks, improving productivity and service uptime.

Led incident analytics that boosted productivity by 70% through real-time issue triaging and escalation.
Developed Tableau dashboards for transaction health checks and SLA monitoring.
Led a 9-member cross-functional team to support critical mainframe application reliability.
Created process improvement solutions that automated 40% of manual tasks in legacy banking operations.
Performed root cause analysis, data validation, and FTP monitoring to ensure data integrity across financial systems.'''
        }
    ],
    'skills': [
        'Product Leadership',
        'Product Roadmapping',
        'Product Strategy',
        'Cross-functional Leadership',
        'Agile & SAFe',
        'AI/ML Integration',
        'Customer Discovery',
        'Cloud Platforms (AWS, Azure)',
        'iPaaS (CloudHub)',
        'MuleSoft Runtime & SDK',
        'Data Analytics',
        'API Integration',
    ],
    'education': [
        {
            'degree': 'Master of Information Systems Management',
            'school': 'Carnegie Mellon University',
            'year': '2017'
        },
        {
            'degree': 'Bachelor of Computer Science and Engineering',
            'school': 'Madan Mohan Malaviya University of Technology',
            'year': '2012'
        }
    ],
    'certifications': [
        {
            'name': 'Microsoft Certified: Azure Fundamentals',
            'issuer': 'Microsoft',
            'date': 'Issued Jun 2020',
            'link': 'https://www.credly.com/badges/25c4a2fc-c738-4f2e-85e4-9b12d1139b90'
        },
        {
            'name': 'GoPractice Product Simulator',
            'issuer': 'GoPractice, Inc',
            'date': 'Issued Aug 2022',
            'link': 'https://www.linkedin.com/learning/certificates/8dc76e1900d2f37b067c7e1bc68f5ff7892f2795e76087b98ceef0ccf123cb18'
        },
        {
            'name': 'Product Management: Building a Product Strategy',
            'issuer': 'LinkedIn Learning',
            'date': 'Issued Jul 2022',
            'link': 'https://www.linkedin.com/learning/certificates/ea6e4022d9ec2cb91be2debd3d6c4d93384244bb3e63c7d31ea51f7f0d4a8880'
        },
        {
            'name': 'AI For Everyone',
            'issuer': 'Coursera – Andrew Ng',
            'date': 'Issued May 2020',
            'link': 'https://www.coursera.org/account/accomplishments/verify/JFEKHQXM8N3S'
        },
        {
            'name': 'Digital Product Management',
            'issuer': 'University of Virginia – Coursera',
            'date': 'Issued Jan 2020',
            'link': 'https://www.coursera.org/account/accomplishments/verify/X7S6EZ5FCR5L'
        }
    ],
    'product_talks_and_articles': [
        {
            'title': 'Featured Speaker – Product School',
            'organization': 'Product School',
            'date': 'Jul 2022 – Sep 2022',
            'description': '''Shared my journey from engineering to product leadership and actionable insights for aspiring PMs. Topics covered included product strategy, roadmap planning, and user-centric thinking.''',
            'link': 'https://www.linkedin.com/video/event/urn:li:ugcPost:6960954001253154818/'
        },
        {
            'title': 'Product Management Blog – Quantitative vs Qualitative Data',
            'organization': 'GoPractice, Inc',
            'date': 'Jul 2022 – Aug 2022',
            'description': '''Explored how product managers can leverage both data types for customer insight and product iteration.''',
            'link': 'https://gopractice.io/data/quantitative-vs-qualitative-data/'
        },
        {
            'title': 'Next-Gen Mule Runtime Release Cadence',
            'organization': 'Salesforce Developer Blog',
            'date': 'Sep 2023',
            'description': '''Announced changes in MuleSoft's release cadence to align with Salesforce updates for developer efficiency.''',
            'link': 'https://developer.salesforce.com/blogs/2023/09/introducing-the-next-gen-mule-runtime-release-cadence'
        },
        {
            'title': 'Featured Speaker – All Things Open Conference',
            'organization': 'All Things Open',
            'date': 'Oct 2022',
            'description': '''Presented on DataWeave at a major open-source conference, engaging the community on enterprise integration patterns and developer tools.''',
            'link': ''
        }
    ],
    'contact': {
        'email': 'pranjal.tripathi18@gmail.com',
        'linkedin': 'https://www.linkedin.com/in/pranjaltripathi/',
        'github': 'https://github.com/pranjaltripathi'
    }
}

# Context processor to make current year available in all templates
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

@app.route('/')
def home():
    return render_template('index.html', profile=PROFILE_DATA)

@app.route('/experience')
def experience():
    return render_template('experience.html', profile=PROFILE_DATA)

@app.route('/products')
def products():
    return render_template('products.html', profile=PROFILE_DATA)

@app.route('/talks')
def talks():
    return render_template('talks.html', profile=PROFILE_DATA)

@app.route('/certifications')
def certifications():
    return render_template('certifications.html', profile=PROFILE_DATA)

@app.route('/contact')
def contact():
    return render_template('contact.html', profile=PROFILE_DATA)

if __name__ == '__main__':
    app.run(debug=True) 