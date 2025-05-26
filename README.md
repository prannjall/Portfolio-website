# Personal Portfolio Website

A modern, responsive portfolio website built with Flask, showcasing professional experience and skills.

## Features

- Responsive design that works on all devices
- Modern UI with smooth animations
- Sections for experience, skills, and education
- Contact information and social media links
- Easy to customize and extend

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/portfolio-website.git
cd portfolio-website
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the development server:
```bash
python app.py
```

5. Visit `http://localhost:5000` in your browser

## Customization

1. Update the `PROFILE_DATA` dictionary in `app.py` with your information
2. Modify the templates in the `templates` directory to change the layout
3. Edit `static/css/style.css` to customize the styling

## Deployment

### Deploying to GitHub Pages

1. Create a new repository on GitHub
2. Push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/portfolio-website.git
git push -u origin main
```

### Deploying to Heroku

1. Create a `Procfile`:
```
web: gunicorn app:app
```

2. Add gunicorn to requirements.txt:
```
gunicorn==20.1.0
```

3. Deploy to Heroku:
```bash
heroku create
git push heroku main
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details. 