# Wagtail CMS Documentation - Technical & General Guide

## Table of Contents
1. [Introduction to Wagtail](#introduction-to-wagtail)
2. [Project Overview](#project-overview)
3. [Project Structure](#project-structure)
4. [Understanding Pages in Wagtail](#understanding-pages-in-wagtail)
5. [Page Creation Flow](#page-creation-flow)
6. [StreamField and Blocks](#streamfield-and-blocks)
7. [Templates and Rendering](#templates-and-rendering)
8. [Project Implementation Details](#project-implementation-details)
9. [Key Concepts](#key-concepts)
10. [Common Questions for Viva](#common-questions-for-viva)

---

## Introduction to Wagtail

### What is Wagtail?
**Wagtail** is a free, open-source content management system (CMS) built on top of Django. It provides a user-friendly interface for managing website content without requiring technical knowledge.

### Key Features:
- **User-friendly Admin Interface**: Non-technical users can easily add and edit content
- **Flexible Content Structure**: Uses StreamField for flexible, modular content blocks
- **Built on Django**: Leverages Django's powerful framework
- **SEO Friendly**: Built-in features for search engine optimization
- **Responsive Design**: Admin interface works on all devices

### Why Wagtail?
- **For Content Editors**: Easy-to-use interface, drag-and-drop content blocks
- **For Developers**: Flexible, extensible, follows Django best practices
- **For Organizations**: Scalable, secure, enterprise-ready

---

## Project Overview

### Project Information
- **Project Title**: Wagtail Custom StreamField Blocks Library
- **Project Type**: Product Developer
- **Student**: Soni Jay Gaurang (Roll No: 240410700159)
- **Year & Section**: 2nd Year
- **Stack**: Python, Django, Wagtail, HTML/CSS, JavaScript, SQLite/PostgreSQL

### Problem Statement

**The Problem:**
Wagtail CMS's standard StreamField lacks custom, reusable content components like FAQ sections, testimonial sliders, and Call-to-Action (CTA) banners. This limitation reduces flexibility and slows content creation for editors who need to build complex, standardized page layouts repeatedly.

**Why It Matters:**
- **For Content Editors**: They must recreate similar content structures manually each time, leading to inconsistent designs and wasted time
- **For Developers**: Without reusable blocks, developers must create custom solutions repeatedly for common content patterns
- **For Organizations**: Inefficient content creation workflows slow down website updates and marketing campaigns

**Real-World Impact:**
This solution addresses a common need in CMS-backed production environments (newsrooms, marketing sites, internal portals) where editors frequently build pages with standardized components.

### Project Goals

**Core Objectives:**
1. Create 3-5 reusable StreamField blocks (FAQ, Testimonials, CTA)
2. Implement proper data validation and structure
3. Develop clean template rendering for each block
4. Build a demo page showcasing all blocks
5. Write comprehensive unit tests
6. Create clear documentation for usage

**Success Metrics:**
- ✅ All custom blocks working as specified
- ✅ High code quality (passing lint, structured code)
- ✅ Good test coverage
- ✅ Clear documentation and demo clarity

### Solution Approach

**What We Built:**
A reusable library of custom StreamField blocks that can be easily integrated into any Wagtail project, allowing content editors to quickly build rich, consistent page layouts without developer intervention.

**Key Features:**
- **FAQBlock**: Question/answer accordion sections with expandable details
- **TestimonialSliderBlock**: Customer testimonials with avatar images and role information
- **CallToActionBlock**: Marketing banners with headlines, body text, and action buttons
- **ImageChooserBlock Integration**: Automatic image resizing for blog posts
- **Template System**: Reusable templates for consistent rendering

---

## Project Structure

### Main Components:

```
mysite/
├── blog/                    # Blog application
│   ├── models.py           # BlogPage and BlogIndexPage models
│   ├── templates/          # HTML templates for blog pages
│   └── migrations/         # Database migrations
├── home/                    # Homepage application
│   ├── models.py           # HomePage model
│   └── templates/          # HTML templates
├── customblocks/           # Custom content blocks library
│   ├── blocks.py          # Block definitions (FAQ, CTA, Testimonials)
│   └── templates/         # Block rendering templates
└── mysite/                  # Main project settings
    └── settings/           # Configuration files
```

### Key Files Explained:

1. **models.py**: Defines page structure and fields
2. **templates/**: HTML files that render pages
3. **migrations/**: Database schema changes
4. **settings.py**: Project configuration

---

## Understanding Pages in Wagtail

### What is a Page?
A **Page** in Wagtail is a Django model that inherits from `wagtail.models.Page`. Each page represents a piece of content on your website.

### Page Hierarchy:
```
Root Page
├── Home Page
├── Blog Index Page
│   ├── Blog Post 1
│   ├── Blog Post 2
│   └── Blog Post 3
└── Other Pages...
```

### Page Types in This Project:

#### 1. **HomePage** (`home/models.py`)
- **Purpose**: Main landing page of the website
- **Fields**:
  - `body`: StreamField containing flexible content blocks
- **Content Blocks Available**:
  - Heading
  - Paragraph (rich text)
  - FAQ Section
  - Testimonial Slider
  - Call to Action

#### 2. **BlogIndexPage** (`blog/models.py`)
- **Purpose**: Lists all blog posts
- **Fields**:
  - `intro`: Rich text introduction

#### 3. **BlogPage** (`blog/models.py`)
- **Purpose**: Individual blog post
- **Fields**:
  - `date`: Publication date
  - `intro`: Short introduction text
  - `body`: StreamField with content blocks
- **Content Blocks Available**:
  - Paragraph (rich text)
  - Image (with automatic resizing)
  - Heading

---

## Page Creation Flow

### Step-by-Step Process:

#### 1. **Define the Model** (models.py)
```python
from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]
```

**What happens here?**
- Defines the data structure for blog posts
- Specifies what fields editors can fill
- Sets up the admin interface panels

#### 2. **Create Database Migration**
```bash
python manage.py makemigrations
python manage.py migrate
```

**What happens here?**
- Django creates SQL commands to update database structure
- Migrations are applied to create/update tables

#### 3. **Create Template** (templates/blog/blog_page.html)
```django
{% extends "base.html" %}
{% load wagtailcore_tags wagtailimages_tags %}

{% block content %}
    <h1>{{ page.title }}</h1>
    <p>{{ page.date }}</p>
    <div>{{ page.intro }}</div>
    
    {% for block in page.body %}
        {% if block.block_type == 'paragraph' %}
            {{ block.value|richtext }}
        {% elif block.block_type == 'image' %}
            {% image block.value width-800 %}
        {% endif %}
    {% endfor %}
{% endblock %}
```

**What happens here?**
- Defines how the page looks on the frontend
- Renders each content block appropriately
- Uses Django template language

#### 4. **Admin Interface**
- Editors go to `/admin/`
- Create new pages through the Wagtail admin
- Fill in fields and add content blocks
- Publish the page

#### 5. **Frontend Display**
- Wagtail automatically routes URLs
- Template renders the page
- Content appears on the website

---

## StreamField and Blocks

### What is StreamField?
**StreamField** is Wagtail's flexible content system that allows editors to build pages using reusable content blocks.

### Why StreamField?
- **Flexibility**: Editors can arrange content in any order
- **Modularity**: Reusable blocks for consistent design
- **No Coding Required**: Editors work visually in admin

### How It Works:

#### 1. **Define Blocks** (customblocks/blocks.py)
```python
class FAQBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False)
    items = blocks.ListBlock(FAQItemBlock())
    
    class Meta:
        template = "customblocks/blocks/faq_block.html"
```

#### 2. **Add to Page Model**
```python
body = StreamField([
    ('faq', FAQBlock()),
    ('cta', CallToActionBlock()),
], use_json_field=True)
```

#### 3. **Render in Template**
```django
{% for block in page.body %}
    {% include_block block %}
{% endfor %}
```

### Block Types in This Project:

1. **FAQBlock**: Question/answer accordion sections
2. **TestimonialSliderBlock**: Customer testimonials with images
3. **CallToActionBlock**: Marketing banners with buttons
4. **ImageChooserBlock**: Image uploads with resizing
5. **RichTextBlock**: Formatted text content

---

## Templates and Rendering

### Template Hierarchy:
```
base.html (main layout)
├── home_page.html (homepage)
├── blog_index_page.html (blog listing)
└── blog_page.html (individual posts)
```

### How Templates Work:

1. **Base Template** (`base.html`)
   - Contains common HTML structure
   - Header, footer, navigation
   - Other templates extend this

2. **Page Templates**
   - Extend base template
   - Define page-specific content
   - Render StreamField blocks

3. **Block Templates** (`customblocks/templates/`)
   - Render individual content blocks
   - Reusable across pages
   - Maintain consistent styling

### Template Tags:

- `{% load wagtailcore_tags %}`: Load Wagtail template tags
- `{% load wagtailimages_tags %}`: Load image handling tags
- `{% pageurl page %}`: Generate page URL
- `{% image %}`: Render images with resizing
- `{% include_block %}`: Render StreamField blocks

---

## Project Implementation Details

### Implementation Flow

#### Phase 1: Project Setup & Planning
1. **Repository Initialization**
   - Set up Django/Wagtail project structure
   - Configure development environment
   - Set up version control (Git)
   - Initialize testing framework (pytest)

2. **Project Architecture Design**
   - Designed modular structure with `customblocks` app
   - Planned separation of concerns (models, templates, template tags)
   - Designed reusable block system

#### Phase 2: Core Block Development

**1. FAQBlock Implementation**

**Problem Solved**: Editors needed a way to create FAQ sections without manually coding accordion structures.

**Implementation**:
```python
# customblocks/blocks.py
class FAQItemBlock(blocks.StructBlock):
    question = blocks.CharBlock(required=True)
    answer = blocks.RichTextBlock(required=True)

class FAQBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, default="Frequently Asked Questions")
    items = blocks.ListBlock(FAQItemBlock())
    
    class Meta:
        template = "customblocks/blocks/faq_block.html"
```

**Features**:
- Nested structure (FAQBlock contains list of FAQItemBlock)
- Uses HTML5 `<details>` and `<summary>` for accessibility
- Template renders as expandable accordion

**2. TestimonialSliderBlock Implementation**

**Problem Solved**: Need for displaying customer testimonials with images in a structured format.

**Implementation**:
```python
class TestimonialBlock(blocks.StructBlock):
    quote = blocks.TextBlock(required=True)
    name = blocks.CharBlock(required=True)
    role = blocks.CharBlock(required=False)
    avatar = ImageChooserBlock(required=False)

class TestimonialSliderBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=False, default="What our customers say")
    testimonials = blocks.ListBlock(TestimonialBlock(), min_num=1)
    
    class Meta:
        template = "customblocks/blocks/testimonial_slider.html"
```

**Features**:
- Supports multiple testimonials in a slider format
- Optional avatar images with automatic resizing
- Structured data (quote, name, role)

**3. CallToActionBlock Implementation**

**Problem Solved**: Need for consistent marketing banners with clear call-to-action buttons.

**Implementation**:
```python
class CallToActionBlock(blocks.StructBlock):
    eyebrow = blocks.CharBlock(required=False)
    headline = blocks.CharBlock(required=True)
    body = blocks.RichTextBlock(required=False)
    button_text = blocks.CharBlock(required=True, default="Get started")
    button_url = blocks.URLBlock(required=True)
    secondary_link_text = blocks.CharBlock(required=False)
    secondary_link_url = blocks.URLBlock(required=False)
    
    class Meta:
        template = "customblocks/blocks/call_to_action.html"
```

**Features**:
- Primary and secondary action buttons
- Rich text body content
- Flexible headline and eyebrow text

#### Phase 3: Integration with Main Project

**BlogPage Integration**:
- Converted `body` field from `RichTextField` to `StreamField`
- Added image upload capability with automatic resizing
- Implemented paragraph, image, and heading blocks
- Created data migration to preserve existing content

**HomePage Integration**:
- Integrated all custom blocks (FAQ, Testimonials, CTA)
- Added basic blocks (heading, paragraph)
- Updated template to render StreamField blocks properly

**Key Implementation Steps**:
1. Created `customblocks` app in main project
2. Copied block definitions and templates
3. Added to `INSTALLED_APPS` in settings
4. Updated page models to use StreamField
5. Created migrations for database changes
6. Updated templates for proper rendering

#### Phase 4: Template System

**Template Structure**:
```
customblocks/templates/customblocks/blocks/
├── faq_block.html          # FAQ accordion rendering
├── testimonial_slider.html # Testimonial display
└── call_to_action.html     # CTA banner rendering
```

**Template Tags**:
- Created `customblocks_tags.py` with utility functions
- `richtext` filter for expanding Wagtail rich text
- `render_streamfield` tag for block rendering

**Rendering Logic**:
- Each block has its own template
- Templates use Django template language
- Supports Wagtail's `{% image %}` tag for images
- Accessible HTML5 semantic elements

#### Phase 5: Image Handling

**Problem Solved**: Need for consistent image sizing across the site.

**Implementation**:
- Blog post images: `width-800` (800px max width)
- Blog index preview: `width-400` (400px max width)
- Testimonial avatars: `fill-80x80` (80x80px with cropping)

**Benefits**:
- Consistent image sizes
- Improved page load performance
- Better user experience
- Reduced bandwidth usage

### Data Flow Architecture

```
Editor Input (Wagtail Admin)
    ↓
StreamField Model (Validation)
    ↓
JSON Serialization (Database Storage)
    ↓
Template Rendering (Frontend Display)
    ↓
HTML Output (User View)
```

### Technical Decisions

**1. Why StreamField?**
- Provides flexibility for content editors
- Stores data as JSON (flexible schema)
- Supports heterogeneous content blocks
- Built-in Wagtail feature (no custom solution needed)

**2. Why Separate `customblocks` App?**
- Reusability across multiple projects
- Separation of concerns
- Easy to maintain and update
- Can be packaged as a reusable library

**3. Why Template-Based Rendering?**
- Consistent styling across blocks
- Easy to customize per project
- Follows Django/Wagtail best practices
- Supports template inheritance

**4. Migration Strategy**
- Created data migration to convert RichTextField to StreamField
- Preserved existing content during migration
- Split migration into data conversion and schema change

### Testing Approach

**Unit Tests** (planned/implemented):
- Block structure validation
- Data serialization correctness
- Template rendering output
- Field validation rules

**Manual Testing**:
- Admin interface usability
- Frontend rendering
- Image resizing
- Cross-browser compatibility

### Project Deliverables

**Code Deliverables**:
- ✅ Custom blocks library (`customblocks` app)
- ✅ Block definitions (`blocks.py`)
- ✅ Template files for rendering
- ✅ Template tags for utilities
- ✅ Integration with BlogPage and HomePage
- ✅ Database migrations

**Documentation Deliverables**:
- ✅ This comprehensive documentation
- ✅ Code comments and docstrings
- ✅ README with setup instructions
- ✅ Usage examples

**Demo Deliverables**:
- ✅ Working demo pages (HomePage, BlogPage)
- ✅ All blocks functional in admin
- ✅ Frontend rendering working correctly

### Challenges Overcome

**1. Migration from RichTextField to StreamField**
- **Challenge**: Existing data in RichTextField format
- **Solution**: Created data migration to convert content to JSON format
- **Result**: Existing content preserved, new structure implemented

**2. Image Resizing**
- **Challenge**: Need for consistent image sizes
- **Solution**: Used Wagtail's built-in image processing with size specifications
- **Result**: Automatic resizing in templates

**3. Template Rendering**
- **Challenge**: Rendering StreamField blocks correctly
- **Solution**: Used `{% include_block %}` tag and custom template logic
- **Result**: Clean, consistent block rendering

**4. Block Integration**
- **Challenge**: Integrating custom blocks into existing pages
- **Solution**: Updated models, created migrations, updated templates
- **Result**: Seamless integration with existing functionality

### Project Impact

**For Content Editors**:
- Faster content creation
- Consistent design across pages
- No coding required
- Easy to use interface

**For Developers**:
- Reusable components
- Clean, maintainable code
- Easy to extend
- Well-documented

**For the Project**:
- Scalable architecture
- Professional implementation
- Production-ready code
- Clear documentation

### Future Enhancements (Stretch Goals)

**If Time Permits**:
1. Live previews in Wagtail admin
2. Block marketplace/sharing mechanism
3. Additional block types (Gallery, Pricing Table, etc.)
4. Advanced styling options
5. Block configuration UI

---

## Key Concepts

### 1. **Models vs Templates**
- **Models**: Define data structure (what data is stored)
- **Templates**: Define presentation (how data is displayed)

### 2. **Content Panels**
- Define which fields appear in admin interface
- Control the editing experience
- Organize fields into logical groups

### 3. **Migrations**
- Track database schema changes
- Version control for database structure
- Allow rollback if needed

### 4. **Page Tree**
- Pages organized hierarchically
- Parent-child relationships
- Automatic URL generation

### 5. **Image Handling**
- Images uploaded through admin
- Automatic resizing with `width-800`, `fill-400x300`, etc.
- Optimized for web performance

---

## Common Questions for Viva

### General Questions:

**Q: What is Wagtail?**
A: Wagtail is a content management system built on Django that allows non-technical users to manage website content through an intuitive admin interface.

**Q: How do pages work in Wagtail?**
A: Pages are Django models that inherit from `Page`. They define fields (like title, date, content) and templates that render them. Editors create pages through the admin interface.

**Q: What is StreamField?**
A: StreamField is Wagtail's flexible content system that lets editors build pages using reusable content blocks (like FAQ sections, images, text) arranged in any order.

**Q: How are images handled?**
A: Images are uploaded through the admin interface and automatically resized using Wagtail's image processing. Templates use `{% image %}` tag with size specifications like `width-800`.

### Technical Questions:

**Q: Explain the page creation flow.**
A: 
1. Define model in `models.py` with fields and StreamField
2. Create database migration (`makemigrations`, `migrate`)
3. Create HTML template to render the page
4. Editors create pages through admin interface
5. Wagtail routes URLs and renders templates

**Q: How does StreamField work?**
A: StreamField stores content as JSON. Each block has a type (like 'paragraph', 'image') and value. Templates iterate through blocks and render each using its template or custom logic.

**Q: What are migrations?**
A: Migrations are Python files that describe database schema changes. They allow version control of database structure and can be applied/rolled back safely.

**Q: How do templates render content?**
A: Templates use Django template language. They extend base templates, iterate through StreamField blocks, and use template tags like `{% image %}` and `{% include_block %}` to render content.

**Q: What is the relationship between models and templates?**
A: Models define the data structure (what fields exist), while templates define how that data is displayed. Models store content, templates present it.

**Q: How are custom blocks created?**
A: Custom blocks are defined in `blocks.py` as classes inheriting from `blocks.StructBlock`. They specify fields and a template. Then added to page models' StreamField and rendered automatically.

### Project-Specific Questions:

**Q: What pages exist in this project?**
A: HomePage (landing page with flexible blocks), BlogIndexPage (lists blog posts), and BlogPage (individual blog posts with images and text).

**Q: What custom blocks are available?**
A: FAQBlock (question/answer sections), TestimonialSliderBlock (customer testimonials), CallToActionBlock (marketing banners), plus standard blocks like images and rich text.

**Q: How are images resized?**
A: Images use Wagtail's image processing. Blog post images are resized to `width-800`, and preview images use `width-400`. This happens automatically when templates render images.

**Q: How is the blog structured?**
A: BlogIndexPage acts as a parent page listing all posts. Each BlogPage is a child page with date, intro, and StreamField body containing paragraphs, images, and headings.

**Q: What problem does this project solve?**
A: This project solves the lack of reusable content components in Wagtail's standard StreamField. It provides custom blocks (FAQ, Testimonials, CTA) that editors can use repeatedly without recreating the same structures manually.

**Q: How did you implement the custom blocks?**
A: Custom blocks were implemented as Django classes inheriting from `blocks.StructBlock`. Each block defines its fields, validation rules, and template. They're added to page models' StreamField and rendered automatically using their templates.

**Q: How did you handle the migration from RichTextField to StreamField?**
A: Created a two-step migration: first converted existing RichTextField content to JSON format (wrapping it in paragraph blocks), then altered the field type to StreamField. This preserved all existing content.

**Q: What is the architecture of your custom blocks library?**
A: The `customblocks` app contains: `blocks.py` (block definitions), `templates/` (rendering templates), and `templatetags/` (utility functions). This modular structure makes it reusable across projects.

**Q: How do images get resized in your project?**
A: Using Wagtail's built-in image processing. Templates specify sizes like `width-800` or `fill-80x80`, and Wagtail automatically generates optimized versions. This happens at render time, not upload time.

---

## Summary

### Key Takeaways:

1. **Wagtail** = Django-based CMS for easy content management
2. **Pages** = Models that define content structure
3. **StreamField** = Flexible content system using blocks
4. **Templates** = HTML files that render pages
5. **Migrations** = Database schema version control

### Workflow:
```
Model Definition → Migration → Template → Admin Interface → Frontend Display
```

### Benefits:
- **For Editors**: Easy content management without coding
- **For Developers**: Flexible, extensible architecture
- **For Users**: Fast, responsive website experience

### Project Summary:

**What We Built:**
- A reusable library of 3 custom StreamField blocks (FAQ, Testimonials, CTA)
- Integration with BlogPage and HomePage
- Automatic image resizing system
- Comprehensive documentation

**How It Works:**
1. Blocks defined in `customblocks/blocks.py`
2. Templates render blocks in `customblocks/templates/`
3. Pages use StreamField to include blocks
4. Editors add blocks through Wagtail admin
5. Frontend renders blocks automatically

**Key Achievements:**
- ✅ All custom blocks functional
- ✅ Clean, maintainable code structure
- ✅ Proper data migrations
- ✅ Image handling implemented
- ✅ Comprehensive documentation

---

*This documentation covers the essential concepts needed for understanding Wagtail CMS and this project's implementation. It serves as both a learning resource and a reference for the Wagtail Custom StreamField Blocks Library project.*

