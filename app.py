import os
from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import database

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")

if not app.secret_key:
    raise RuntimeError("SECRET_KEY environment variable is not set")
# Ensure database is initialized
database.init_db()

# Detailed Wikipedia Bio Data for Shri Akhilesh Yadav
AKHILESH_YADAV_BIO = {
    "name": "Shri Akhilesh Yadav",
    "hindi_name": "श्री अखिलेश यादव",
    "title": "National President, Samajwadi Party & Member of Parliament",
    "cm_title": "20th Chief Minister of Uttar Pradesh (2012–2017)",
    "born": "1 July 1973 (Age 52)",
    "birthplace": "Saifai, Etawah, Uttar Pradesh, India",
    "father": "Late Shri Mulayam Singh Yadav (Founder of Samajwadi Party, Former Defence Minister of India)",
    "mother": "Late Smt. Malti Devi",
    "spouse": "Smt. Dimple Yadav (Member of Parliament, Lok Sabha)",
    "children": "Aditi Yadav, Tina Yadav, Arjun Yadav",
    "education": [
        {
            "institution": "Dholpur Military School, Rajasthan",
            "degree": "Senior Secondary Military & Leadership Education",
            "highlight": "Rigorous discipline and physical training foundation"
        },
        {
            "institution": "Sri Jayachamarajendra College of Engineering (SJCE), Mysore",
            "degree": "Bachelor of Engineering (B.E.) in Civil / Environmental Engineering",
            "highlight": "Engineering mindset for large-scale infrastructure planning"
        },
        {
            "institution": "University of Sydney, Australia",
            "degree": "Master’s Degree in Environmental Engineering",
            "highlight": "Global perspective on sustainable cities, ecology and clean energy"
        }
    ],
    "political_timeline": [
        {
            "year": "2000",
            "role": "Elected Member of Parliament (Kannauj, 13th Lok Sabha)",
            "details": "Entered Parliament at age 27 following a historic by-election victory."
        },
        {
            "year": "2004 & 2009",
            "role": "Re-elected to 14th & 15th Lok Sabha",
            "details": "Consecutively represented Kannauj and Firozabad, focusing on rural development and youth issues."
        },
        {
            "year": "2012–2017",
            "role": "20th Chief Minister of Uttar Pradesh",
            "details": "Assumed office on 15 March 2012 at age 38, becoming the youngest person ever to lead Uttar Pradesh."
        },
        {
            "year": "2017–Present",
            "role": "National President, Samajwadi Party",
            "details": "Spearheading the socialist movement, championing secularism, farmer rights, and constitutional defense."
        },
        {
            "year": "2022–2024",
            "role": "Leader of Opposition, UP Legislative Assembly",
            "details": "Held the government accountable on employment, paper leaks, inflation, and caste census."
        },
        {
            "year": "2024–Present",
            "role": "Member of Parliament, 18th Lok Sabha (Kannauj)",
            "details": "Elected with a resounding mandate, leading the PDA alliance in national parliament."
        }
    ],
    "legacy_milestones": [
        {
            "name": "Agra-Lucknow Expressway (302 km)",
            "desc": "Built in record 23 months. Features India's first 3.3 km runway for IAF fighter jets (Mirage 2000 & Sukhoi Su-30MKI)."
        },
        {
            "name": "Free Laptop Distribution Scheme",
            "desc": "Empowered over 18 lakh students with free branded laptops, bridging the generational digital divide."
        },
        {
            "name": "1090 Women Power Line",
            "desc": "24x7 confidential distress line for women safety, handling millions of complaints with female operators."
        },
        {
            "name": "UP 100 / Dial 112 Modern Policing",
            "desc": "Pioneered integrated GPS police response fleet reaching urban emergencies within 15 minutes."
        },
        {
            "name": "Lucknow Metro & Transit",
            "desc": "Fastest executed metro rail project in India, connecting Chaudhary Charan Singh Airport to Munshi Pulia."
        },
        {
            "name": "Gomti Riverfront & Janeshwar Mishra Park",
            "desc": "Asia's largest eco-park (376 acres) with solar illumination, cycle tracks, and river rejuvenation."
        },
        {
            "name": "Medanta & Cancer Super-Specialty Hospitals",
            "desc": "Brought top-tier tertiary healthcare infrastructure to public reach in Lucknow and central UP."
        }
    ]
}

EVENTS_DATA = [
    {
        "id": "summit-blr",
        "title": "Vision India Startup Summit 2025",
        "date": "November 16, 2025",
        "time": "10:00 AM - 5:00 PM IST",
        "location": "Taj Bangalore, Karnataka",
        "category": "Technology & Entrepreneurship",
        "description": "Bengaluru, the innovation capital, hosts a gathering of India's brightest entrepreneurial minds, thought leaders, policymakers, and youth innovators led by Shri Akhilesh Yadav.",
        "badge": "Flagship Event"
    },
    {
        "id": "youth-conclave-lko",
        "title": "National Youth Leadership Conclave",
        "date": "December 05, 2025",
        "time": "11:00 AM - 4:00 PM IST",
        "location": "Indira Gandhi Pratishthan, Lucknow",
        "category": "Youth & Employment",
        "description": "Engaging students, researchers, and early-career innovators to shape employment policies, skill-tech integration, and digital public goods.",
        "badge": "Upcoming"
    },
    {
        "id": "kisan-samvad-varanasi",
        "title": "Samriddh Kisan, Sashakt Bharat Samvad",
        "date": "December 22, 2025",
        "time": "09:30 AM - 3:00 PM IST",
        "location": "Varanasi, Uttar Pradesh",
        "category": "Agriculture & Rural Economy",
        "description": "Deliberating on legally guaranteed MSP, modern cold-chain logistics, agro-processing clusters, and direct income stability for farmers.",
        "badge": "Policy Dialogue"
    }
]

ACHIEVEMENTS_DATA = [
    {
        "title": "Agra-Lucknow Expressway",
        "category": "World-Class Infrastructure",
        "stat": "302 km",
        "description": "Built in record 23 months. Features India's first dedicated 3.3 km runway for IAF fighter aircraft landings during national emergencies.",
        "icon": "route",
        "highlight": "Record Speed Construction"
    },
    {
        "title": "Free Laptop Distribution Scheme",
        "category": "Digital Empowerment",
        "stat": "18+ Lakh Laptops",
        "description": "World's largest digital inclusion initiative distributing free branded laptops with multilingual OS to matriculate and intermediate students.",
        "icon": "laptop",
        "highlight": "Bridged the Digital Divide"
    },
    {
        "title": "1090 Women Power Line & UP 100/112",
        "category": "Citizen Security & Tech",
        "stat": "24x7 Response",
        "description": "Pioneered integrated high-tech emergency response systems, distress dispatch, and specialized women safety helpline empowering millions.",
        "icon": "shield-check",
        "highlight": "Modern Policing Benchmark"
    },
    {
        "title": "Lucknow Metro Rail",
        "category": "Urban Mass Transit",
        "stat": "Fastest Metro Rollout",
        "description": "State-of-the-art clean, rapid mass urban transit engineered to decongest historical Lucknow, connecting airport to city centers efficiently.",
        "icon": "train",
        "highlight": "Clean & Sustainable Transit"
    },
    {
        "title": "Gomti Riverfront & Janeshwar Mishra Park",
        "category": "Green Ecology & Urban Spaces",
        "stat": "376 Acres",
        "description": "Created Asia's largest eco-park with solar-powered illumination, cycling tracks, and ecological river rejuvenation projects.",
        "icon": "trees",
        "highlight": "Ecological Restoration"
    },
    {
        "title": "Super-Specialty Healthcare (Medanta & Cancer Hospital)",
        "category": "Public Healthcare",
        "stat": "Thousands of Beds",
        "description": "Established world-class tertiary healthcare centers, specialized oncology institutes, and 108/102 rural ambulance networks.",
        "icon": "activity",
        "highlight": "Affordable Quality Care"
    }
]

PRESS_PHOTOS = [
    {
        "filename": "akhilesh_press_1.jpg",
        "title": "Press Conference at Samajwadi Party HQ, Lucknow",
        "topic": "Constitutional Integrity & Electoral Democracy",
        "date": "June 26, 2025",
        "source": "Getty Images / Hindustan Times"
    },
    {
        "filename": "akhilesh_press_2.jpg",
        "title": "National Media Address on Election Outcomes",
        "topic": "Voter Rights & Judicial Safeguards",
        "date": "May 6, 2026",
        "source": "Getty Images / Hindustan Times"
    },
    {
        "filename": "akhilesh_press_3.jpg",
        "title": "Press Briefing on Nari Shakti & Women Representation",
        "topic": "Women Autonomy & Social Justice",
        "date": "April 19, 2026",
        "source": "Getty Images / Hindustan Times"
    },
    {
        "filename": "akhilesh_press_4.jpg",
        "title": "Media Interaction on Farmer MSP & Youth Jobs",
        "topic": "Economic Sovereignty & Employment",
        "date": "April 19, 2026",
        "source": "Getty Images / Hindustan Times"
    }
]

@app.route("/")
def index():
    return render_template(
        "index.html", 
        events=EVENTS_DATA[:2], 
        achievements=ACHIEVEMENTS_DATA[:4],
        bio=AKHILESH_YADAV_BIO,
        press_photos=PRESS_PHOTOS
    )

@app.route("/akhilesh-yadav")
@app.route("/leader")
def akhilesh_yadav():
    return render_template("akhilesh_yadav.html", bio=AKHILESH_YADAV_BIO, press_photos=PRESS_PHOTOS)

@app.route("/blueprint")
def blueprint():
    return render_template("blueprint.html")

@app.route("/achievements")
def achievements():
    return render_template("achievements.html", achievements=ACHIEVEMENTS_DATA)

@app.route("/events")
def events():
    return render_template("events.html", events=EVENTS_DATA)

@app.route("/volunteer")
def volunteer():
    return render_template("volunteer.html")

@app.route("/api/volunteer", methods=["POST"])
def api_volunteer():
    try:
        data = request.form
        full_name = data.get("full_name", "").strip()
        email = data.get("email", "").strip()
        phone = data.get("phone", "").strip()
        state = data.get("state", "").strip()
        district = data.get("district", "").strip()
        interest_area = data.get("interest_area", "General")
        message = data.get("message", "").strip()

        if not full_name or not email or not phone:
            return jsonify({"status": "error", "message": "Please provide full name, email, and phone number."}), 400

        database.add_volunteer(full_name, email, phone, state, district, interest_area, message)
        return jsonify({"status": "success", "message": "Thank you for joining the PDA movement! Our team will connect with you soon."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/rsvp", methods=["POST"])
def api_rsvp():
    try:
        data = request.form
        event_name = data.get("event_name", "").strip()
        full_name = data.get("full_name", "").strip()
        email = data.get("email", "").strip()
        phone = data.get("phone", "").strip()
        occupation = data.get("occupation", "").strip()
        city = data.get("city", "").strip()

        if not full_name or not email or not phone or not event_name:
            return jsonify({"status": "error", "message": "All required fields must be filled."}), 400

        database.add_event_rsvp(event_name, full_name, email, phone, occupation, city)
        return jsonify({"status": "success", "message": f"RSVP confirmed for '{event_name}'! We look forward to meeting you."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/api/contact", methods=["POST"])
def api_contact():
    try:
        data = request.form
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        phone = data.get("phone", "").strip()
        subject = data.get("subject", "General Inquiry").strip()
        message = data.get("message", "").strip()

        if not name or not email or not message:
            return jsonify({"status": "error", "message": "Please fill name, email, and message."}), 400

        database.add_contact_message(name, email, phone, subject, message)
        return jsonify({"status": "success", "message": "Your message has been received. Thank you for connecting with Team Vision India!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/admin")
def admin():
    stats = database.get_stats()
    return render_template("admin.html", stats=stats)

if __name__ == "__main__":
    print("=" * 60)
    print(" VISION INDIA | PDA WEB PORTAL")
    print(" Running on http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, host="127.0.0.1", port=5000)
