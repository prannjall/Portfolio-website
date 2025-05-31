# Professional Portfolio Website

A modern, responsive portfolio website built with Flask and Bootstrap, featuring a clean and professional design.

## Features

- **Modern Design**: Clean, professional layout with smooth animations and transitions
- **Responsive**: Fully responsive design that works on all devices
- **Dynamic Content**: Content managed through a Python profile configuration
- **Multiple Sections**:
  - Hero section with professional background
  - Core Competencies with custom icons
  - Professional Experience with company logos
  - Featured Products showcase
  - Talks & Articles with category-specific icons
  - Certifications with custom icons
  - Education history

## Tech Stack

- **Backend**: Python/Flask
- **Frontend**: 
  - HTML5
  - CSS3
  - Bootstrap 5
  - Font Awesome icons
- **Images**: 
  - Custom icons from Flaticon
  - Professional background images
  - Company logos
  - Product images

## Project Structure

```
portfolio/
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       ├── background.jpg
│       ├── profile.jpg
│       ├── companies/
│       └── products/
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── experience.html
│   ├── products.html
│   ├── talks.html
│   ├── certifications.html
│   └── contact.html
├── app.py
├── profile.py
└── README.md
```

## Setup and Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd portfolio
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

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to `http://localhost:5000`

## Customization

### Profile Information
Edit `profile.py` to update your personal information, including:
- Name and title
- Professional summary
- Skills and competencies
- Work experience
- Products
- Talks and articles
- Certifications
- Education
- Contact information

### Styling
- Main styles are in `static/css/style.css`
- Bootstrap classes are used throughout for responsive design
- Custom styling can be added inline or in the CSS file

### Images
- Profile picture: Replace `static/images/profile.jpg`
- Background image: Replace `static/images/background.jpg`
- Company logos: Add to `static/images/companies/`
- Product images: Add to `static/images/products/`

## Features in Detail

### Hero Section
- Professional dark background with overlay
- Centered profile image with border
- Name and title with text shadow
- Italicized professional summary

### Core Competencies
- Grid layout with custom icons
- Hover effects on cards
- Category-specific icons for each skill

### Experience Section
- Company logos with consistent sizing
- Duration and location badges
- Bullet points for responsibilities
- Responsive grid layout

### Products Section
- Featured products with custom images
- Technology badges
- Consistent image sizing
- Clean card layout

### Talks & Articles
- Category-specific icons
- Date badges
- Organization information
- Truncated descriptions

### Certifications
- Custom icons for each certification type
- Issuer and date information
- Clean layout with icons

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Icons from [Flaticon](https://www.flaticon.com)
- Background images from [Unsplash](https://unsplash.com)
- Bootstrap framework
- Font Awesome icons

## Contact

Pranjal Tripathi - [LinkedIn](https://www.linkedin.com/in/pranjaltripathi/)

Project Link: [https://github.com/pranjaltripathi/portfolio-website](https://github.com/pranjaltripathi/portfolio-website) 
