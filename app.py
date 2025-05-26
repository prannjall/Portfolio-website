from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.urandom(24)

# Profile data
PROFILE_DATA = {
    'name': 'Pranjal Tripathi',
    'title': 'Senior Product Manager at Salesforce',
    'summary': '''Pranjal Tripathi is a Senior Product Manager at Salesforce with over 10 years of experience in product management. He has a proven track record of using creativity and customer feedback to launch successful products that align with the company's vision.

Pranjal's expertise in product management includes creating product roadmaps, achieving product market fit, defining product strategy and vision, and leading cross-functional teams. He also has a strong understanding of user experience and a talent for strategic planning and features prioritization.

Pranjal started his career as a Product Data Analyst at Tata Consultancy Services, where he worked on projects for MUFG Union Bank and BestBuy. He also has experience working on product teams at Deloitte and ServiceLink. Pranjal's strong market understanding, analytical skills, and strategic thinking enable him to lead his team to build the right features for their customer base. He is also known for his excellent people management and leadership skills.''',
    'experience': [
        {
            'title': 'Senior Product Manager - CloudHub',
            'company': 'Salesforce',
            'duration': 'Aug 2024 - Present',
            'location': 'Seattle, Washington, United States · Hybrid',
            'description': '''About Products:
* Cloudhub is an (iPasS) Integrated platform as a service which is multi-tenant, secure, highly available service where customers can deploy integration application on cloud also integrate on-premise application with cloud services.
* The Anypoint Virtual Private Cloud (VPC) offering allows you to create a virtual, private, and isolated network segment in the cloud to host your CloudHub workers.
* CloudHub dedicated load balancers (DLBs) enable customers to route external HTTP/HTTPS traffic to multiple Mule applications deployed to CloudHub workers in a VPC.
* Anypoint VPN is used to create a secure connection between your MuleSoft VPC and customers on-premises network.
* AWS Transit Gateway acts as a cloud router in AWS, simplifying network access between VPCs, on-premises data centers, and 3rd-party software, while providing increased visibility and control over the network.

Responsibilities:
• Developing and implementing product strategies consistent with company vision.
• Collaborating with senior management to create product plans and roadmaps.
• Collecting and analyzing feedback from customers, stakeholders and other teams to enhance features and products.
• Translating product strategy into detailed requirements, user stories, and prototypes.
• Engaging with diverse partners – sales, marketing, services, operations, support, documentation, engineering – to help define and deliver the best customer journey
• Making creative recommendations to reduce customer's pain-points and improve their experience.
• Tracking product usage, impact, heath and performance by monitoring product metrics and key performance Indicators (KPIs).
• Ensuring product releases are launched correctly/on schedule while driving field enablement activities.
• Engaging with customers and partners to deliver roadmap updates, get product feedback, and identify additional challenges and opportunities.'''
        },
        {
            'title': 'Senior Product Manager - Mule Runtime, HTTP Connector & Mule SDK',
            'company': 'Salesforce',
            'duration': 'Mar 2023 - Present',
            'location': 'Seattle, Washington, United States · Remote',
            'description': '''About Products:
* MuleSoft Runtime engine (Mule) is the lightweight integration runtime engine that allows you to connect anything, anywhere.
* Anypoint Connector for HTTP (HTTP Connector) enables you to declare HTTP servers that listen to requests and trigger flows.
* Mule SDK (Java SDK and XML SDK) provides a set of tools/APIs for faster development of connectors or modules.

Responsibilities:
• Developing and implementing product strategies consistent with company vision.
• Working with senior management to create product plans and roadmaps.
• Collecting and analyzing feedback from customers, stakeholders and other teams to enhance features and products.
• Making creative recommendations to reduce customer's pain-points and improve their experience.
• Tracking product use, impact, heath and performance by monitoring product metrics and key performance Indicators (KPIs).
• Ensuring products and releases are launched correctly and on schedule.
• Keeping customers up to date by reviewing and maintaining updated product documentations.'''
        },
        {
            'title': 'Senior Product Manager - DataWeave, Mule SDK, Mule Migration Assistant (MMA) & End Of Life Mule 3.x',
            'company': 'Salesforce',
            'duration': 'Sep 2022 - Apr 2023',
            'location': 'Pittsburgh, Pennsylvania, United States',
            'description': '''About Products:
* DataWeave is the programming language designed by MuleSoft for data transformation.
* Mule SDK provides a set of tools/APIs for faster development of connectors or modules.
* Mule Migration Assistant (MMA) help customers easily migrate their apps from one Mule version to another.
* Managed the End Of Life of Mule Runtime 3.x versions.'''
        },
        {
            'title': 'Senior Product Manager',
            'company': 'ServiceLink',
            'duration': 'Jul 2020 - Feb 2022',
            'location': 'Pittsburgh, Pennsylvania, United States',
            'description': '''• Ensured that various stages of product development are completed on time by leading, organizing and requesting constant updates from cross-functional teams.
• Conceptualized and translated ideas into product designs and led a team to launch these products into the world, taking responsibility for adoption of products.
• Defined and contributed to the product vision, roadmap and OKRs while executing product strategy at a tactical level.
• Developed and implemented product strategies consistent with company vision.
• Collected and analyzed feedback from customers, stakeholders and other teams to shape requirements, features and end products.'''
        }
    ],
    'skills': [
        'Product Management',
        'Agile Methodologies',
        'Team Leadership',
        'Strategic Planning',
        'User Experience',
        'Data Analytics',
        'Stakeholder Management',
        'Product Strategy',
        'Feature Prioritization',
        'Product Roadmapping',
        'AI/ML',
        'NLP',
        'Data Science',
        'Machine Learning',
        'Cloud Computing',
        'AWS',
        'Azure'
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
            'year': '2015'
        }
    ],
    'contact': {
        'email': 'pranjaltripathi@example.com',
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

@app.route('/projects')
def projects():
    return render_template('projects.html', profile=PROFILE_DATA)

@app.route('/contact')
def contact():
    return render_template('contact.html', profile=PROFILE_DATA)

if __name__ == '__main__':
    app.run(debug=True) 