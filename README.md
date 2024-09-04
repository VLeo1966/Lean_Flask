# Lean_Fla# Flask Website with Bootstrap

This repository contains a simple Flask web application with three routes and Bootstrap integration for basic styling. The app includes a homepage, a blog page, and a contacts page. The layout is responsive, thanks to Bootstrap, and has an easy-to-navigate structure with dynamic content rendering.

## Project Structure

```
.
├── static
│   ├── css
│   │   └── styles.css    # Custom CSS styles
│   └── images            # Images for the blog and homepage
├── templates
│   ├── index.html        # Main page (Home)
│   ├── blog.html         # Blog page
│   └── contacts.html     # Contacts page
├── app.py                # Flask application
├── README.md             # Project documentation
└── requirements.txt      # List of dependencies
```

## Prerequisites

- Python 3.x
- Flask (`pip install Flask`)
- Bootstrap (CDN included in HTML templates)

## Getting Started

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/flask-bootstrap-website.git
cd flask-bootstrap-website
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the App

1. Start the Flask development server:

```bash
python app.py
```

2. Open your browser and go to:

```
http://127.0.0.1:5000/
```

### Routes

- `/` - Main page with a welcoming banner and a button to visit the blog.
- `/blog/` - Blog page displaying articles with images.
- `/contacts/` - Contacts page with detailed information.

## Templates

### `index.html` (Home)

- Uses a Bootstrap navbar for easy navigation between pages.
- Displays a hero banner with a call to action.

### `blog.html` (Blog)

- Contains a grid of blog articles with images, titles, descriptions, and a "Read more" button.

### `contacts.html` (Contacts)

- Displays contact information in a simple, organized layout.
- Social media links, email, address, and phone are provided.

### Custom Styles

- The `styles.css` file in `static/css/` contains custom styles for the hero banner and contact page layout.

## Bootstrap

The project uses Bootstrap 4.5 via CDN for styling and responsiveness. The navigation bar and page layouts adapt to different screen sizes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Feel free to customize the content and design as per your needs.sk