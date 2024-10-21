# Defining careers
careers = {
    'Data Scientist': {
        'skills': {'programming': 0.9, 'data analysis': 0.9, 'statistics': 0.8, 'machine learning': 0.7,
                   'communication': 0.6},
        'education': ['Computer Science', 'Mathematics', 'Statistics', 'Data Science'],
        'work_style': ['remote', 'hybrid', 'office'],
        '': ['tech', 'finance', 'healthcare', 'e-commerce', 'consulting'],
        'description': "Data scientists analyze complex data to provide actionable insights. They use advanced analytics, machine learning, and statistical methods to solve business problems."
    },
    'Software Engineer': {
        'skills': {'programming': 0.9, 'problem-solving': 0.8, 'algorithms': 0.7, 'system design': 0.7,
                   'debugging': 0.8},
        'education': ['Computer Science', 'Software Engineering', 'Information Technology'],
        'work_style': ['remote', 'hybrid', 'office'],
        'industries': ['tech', 'finance', 'healthcare', 'gaming', 'cybersecurity'],
        'description': "Software engineers design, develop, and maintain software systems and applications. They work on various stages of the software development lifecycle."
    },
    'UI/UX Designer': {
        'skills': {'design': 0.9, 'creativity': 0.8, 'prototyping': 0.7, 'user research': 0.7, 'wireframing': 0.8},
        'education': ['Design', 'Human-Computer Interaction', 'Psychology'],
        'work_style': ['remote', 'hybrid', 'office'],
        'industries': ['tech', 'media', 'advertising', 'e-commerce', 'consulting'],
        'description': "UI/UX Designers focus on creating user-friendly interfaces and experiences. They combine creativity with user research to design intuitive digital products."
    },
    'Financial Analyst': {
        'skills': {'financial analysis': 0.9, 'data interpretation': 0.8, 'accounting': 0.7, 'Excel': 0.8,
                   'financial modeling': 0.7},
        'education': ['Finance', 'Economics', 'Accounting', 'Business Administration'],
        'work_style': ['office', 'hybrid'],
        'industries': ['finance', 'banking', 'investment', 'insurance', 'corporate finance'],
        'description': "Financial analysts evaluate financial data, market trends, and investment opportunities to help businesses and individuals make informed financial decisions."
    },
    'Marketing Manager': {
        'skills': {'marketing strategy': 0.9, 'communication': 0.8, 'project management': 0.7, 'data analysis': 0.6,
                   'creativity': 0.7},
        'education': ['Marketing', 'Business Administration', 'Communications'],
        'work_style': ['office', 'hybrid', 'remote'],
        'industries': ['advertising', 'tech', 'retail', 'media', 'consumer goods'],
        'description': "Marketing managers develop and implement marketing strategies to promote products or services. They oversee marketing campaigns and analyze their effectiveness."
    },
    'Nurse Practitioner': {
        'skills': {'patient care': 0.9, 'medical knowledge': 0.9, 'communication': 0.8, 'decision making': 0.8,
                   'empathy': 0.9},
        'education': ['Nursing', 'Advanced Practice Nursing'],
        'work_style': ['on-site'],
        'industries': ['healthcare', 'hospitals', 'clinics', 'private practice'],
        'description': "Nurse practitioners provide advanced nursing care, including diagnosing and treating illnesses, prescribing medication, and educating patients on health and wellness."
    },
    'Environmental Scientist': {
        'skills': {'data analysis': 0.8, 'research': 0.9, 'environmental regulations': 0.7, 'field work': 0.7,
                   'report writing': 0.8},
        'education': ['Environmental Science', 'Biology', 'Chemistry', 'Geology'],
        'work_style': ['field work', 'office', 'hybrid'],
        'industries': ['environmental consulting', 'government', 'non-profit', 'research institutions'],
        'description': "Environmental scientists study the environment and how it's affected by human activities. They work on protecting natural resources and solving environmental problems."
    },
    'Cybersecurity Analyst': {
        'skills': {'network security': 0.9, 'threat detection': 0.8, 'risk assessment': 0.7, 'programming': 0.7,
                   'problem-solving': 0.8},
        'education': ['Computer Science', 'Information Security', 'Cybersecurity'],
        'work_style': ['office', 'hybrid', 'remote'],
        'industries': ['tech', 'finance', 'government', 'healthcare', 'consulting'],
        'description': "Cybersecurity analysts protect computer networks and systems from cyber threats. They monitor for security breaches and implement measures to protect sensitive information."
    },
    'Teacher': {
        'skills': {'instruction': 0.9, 'communication': 0.9, 'patience': 0.8, 'organization': 0.7, 'adaptability': 0.8},
        'education': ['Education', 'Subject-specific degree'],
        'work_style': ['on-site', 'hybrid'],
        'industries': ['education', 'online learning', 'tutoring', 'educational content creation'],
        'description': "Teachers educate students in various subjects and grade levels. They develop lesson plans, assess student progress, and create a positive learning environment."
    },
    'Mechanical Engineer': {
        'skills': {'CAD software': 0.9, 'problem-solving': 0.8, 'technical drawing': 0.7, 'project management': 0.6,
                   'analytical skills': 0.8},
        'education': ['Mechanical Engineering', 'Engineering'],
        'work_style': ['office', 'field work', 'hybrid'],
        'industries': ['manufacturing', 'automotive', 'aerospace', 'energy', 'robotics'],
        'description': "Mechanical engineers design, develop, and test mechanical devices, including tools, engines, and machines. They work on projects from concept through production."
    },
    'Graphic Designer': {
        'skills': {'design software': 0.9, 'creativity': 0.9, 'typography': 0.7, 'color theory': 0.8,
                   'visual communication': 0.8},
        'education': ['Graphic Design', 'Fine Arts', 'Visual Communications'],
        'work_style': ['remote', 'hybrid', 'office'],
        'industries': ['advertising', 'media', 'publishing', 'tech', 'branding agencies'],
        'description': "Graphic designers create visual concepts using computer software or by hand to communicate ideas that inspire, inform, or captivate consumers."
    },
    'Registered Nurse': {
        'skills': {'patient care': 0.9, 'medical knowledge': 0.8, 'communication': 0.9, 'critical thinking': 0.8,
                   'empathy': 0.9},
        'education': ['Nursing'],
        'work_style': ['on-site'],
        'industries': ['healthcare', 'hospitals', 'clinics', 'nursing homes', 'schools'],
        'description': "Registered nurses provide and coordinate patient care, educate patients and the public about various health conditions, and provide advice and emotional support to patients and their families."
    },
    'Sales Manager': {
        'skills': {'leadership': 0.9, 'negotiation': 0.8, 'communication': 0.9, 'customer service': 0.8,
                   'strategic planning': 0.7},
        'education': ['Business Administration', 'Marketing', 'Communications'],
        'work_style': ['office', 'field work', 'hybrid'],
        'industries': ['retail', 'tech', 'real estate', 'pharmaceutical', 'manufacturing'],
        'description': "Sales managers direct organizations' sales teams. They set sales goals, analyze data, and develop training programs for sales representatives."
    },
    'Civil Engineer': {
        'skills': {'structural analysis': 0.9, 'project management': 0.8, 'CAD software': 0.8, 'problem-solving': 0.8,
                   'mathematics': 0.7},
        'education': ['Civil Engineering', 'Engineering'],
        'work_style': ['office', 'field work', 'hybrid'],
        'industries': ['construction', 'government', 'consulting', 'transportation', 'environmental'],
        'description': "Civil engineers design, construct, supervise, operate, and maintain large infrastructure projects and systems, including roads, buildings, airports, tunnels, dams, bridges, and water supply and sewage systems."
    },
    'Human Resources Manager': {
        'skills': {'interpersonal communication': 0.9, 'conflict resolution': 0.8, 'organizational skills': 0.8,
                   'employee relations': 0.9, 'recruitment': 0.7},
        'education': ['Human Resources', 'Business Administration', 'Psychology'],
        'work_style': ['office', 'hybrid'],
        'industries': ['corporate', 'consulting', 'healthcare', 'education', 'non-profit'],
        'description': "Human resources managers plan, coordinate, and direct the administrative functions of an organization. They oversee recruitment, interviewing, and hiring of new staff; consult with top executives on strategic planning; and serve as a link between an organization's management and its employees."
    },
    'Architect': {
        'skills': {'design': 0.9, 'CAD software': 0.8, 'project management': 0.7, 'spatial awareness': 0.9,
                   'building codes knowledge': 0.8},
        'education': ['Architecture', 'Environmental Design'],
        'work_style': ['office', 'field work', 'hybrid'],
        'industries': ['architecture firms', 'construction', 'real estate development', 'government',
                       'interior design'],
        'description': "Architects plan and design houses, office buildings, and other structures. They combine art and science to create functional and aesthetically pleasing buildings and environments."
    },
    'Chef': {
        'skills': {'cooking techniques': 0.9, 'menu planning': 0.8, 'food safety': 0.9, 'leadership': 0.8,
                   'creativity': 0.8},
        'education': ['Culinary Arts', 'Food Science'],
        'work_style': ['on-site'],
        'industries': ['restaurants', 'hotels', 'catering', 'cruise ships', 'personal chef services'],
        'description': "Chefs oversee the daily food preparation at restaurants and other places where food is served. They direct kitchen staff and handle any food-related concerns."
    },
    'Electrician': {
        'skills': {'electrical systems': 0.9, 'troubleshooting': 0.8, 'hand-eye coordination': 0.8,
                   'reading blueprints': 0.7, 'safety procedures': 0.9},
        'education': ['Vocational Training', 'Apprenticeship'],
        'work_style': ['field work', 'on-site'],
        'industries': ['construction', 'maintenance', 'manufacturing', 'residential services', 'renewable energy'],
        'description': "Electricians install, maintain, and repair electrical power, communications, lighting, and control systems in homes, businesses, and factories."
    },
    'Psychologist': {
        'skills': {'active listening': 0.9, 'analysis': 0.8, 'patience': 0.9, 'communication': 0.9, 'empathy': 0.9},
        'education': ['Psychology', 'Counseling'],
        'work_style': ['office', 'remote'],
        'industries': ['healthcare', 'private practice', 'schools', 'research institutions', 'corporate'],
        'description': "Psychologists study cognitive, emotional, and social processes and behavior by observing, interpreting, and recording how individuals relate to one another and to their environments."
    },
    'Veterinarian': {
        'skills': {'animal care': 0.9, 'diagnosis': 0.9, 'surgery': 0.8, 'communication': 0.8, 'compassion': 0.9},
        'education': ['Veterinary Medicine'],
        'work_style': ['on-site'],
        'industries': ['veterinary clinics', 'zoos', 'wildlife rehabilitation', 'research', 'farm animal care'],
        'description': "Veterinarians care for the health of animals and work to improve public health. They diagnose, treat, and research medical conditions and diseases of pets, livestock, and other animals."
    },
    'Journalist': {
        'skills': {'writing': 0.9, 'research': 0.8, 'interviewing': 0.8, 'critical thinking': 0.8,
                   'time management': 0.7},
        'education': ['Journalism', 'Communications', 'English'],
        'work_style': ['field work', 'remote', 'office'],
        'industries': ['news media', 'publishing', 'online media', 'television', 'radio'],
        'description': "Journalists inform the public about news and events happening internationally, nationally, and locally. They report the news for newspapers, magazines, websites, television, and radio."
    },
    'Physical Therapist': {
        'skills': {'anatomy knowledge': 0.9, 'patient care': 0.9, 'exercise science': 0.8, 'communication': 0.8,
                   'problem-solving': 0.7},
        'education': ['Physical Therapy', 'Exercise Science'],
        'work_style': ['on-site'],
        'industries': ['healthcare', 'sports', 'rehabilitation centers', 'nursing homes', 'home health services'],
        'description': "Physical therapists help injured or ill people improve their movement and manage their pain. They are often an important part of rehabilitation and treatment of patients with chronic conditions or injuries."
    },
    'Accountant': {
        'skills': {'financial reporting': 0.9, 'analytical skills': 0.8, 'attention to detail': 0.9,
                   'tax law knowledge': 0.8, 'mathematics': 0.7},
        'education': ['Accounting', 'Finance', 'Business Administration'],
        'work_style': ['office', 'remote', 'hybrid'],
        'industries': ['accounting firms', 'corporate', 'government', 'non-profit', 'financial services'],
        'description': "Accountants prepare and examine financial records. They ensure that financial records are accurate and that taxes are paid properly and on time. They assess financial operations and work to help ensure that organizations run efficiently."
    },
    'Pharmacist': {
        'skills': {'pharmacology': 0.9, 'patient counseling': 0.8, 'attention to detail': 0.9, 'communication': 0.8,
                   'medical ethics': 0.8},
        'education': ['Pharmacy'],
        'work_style': ['on-site'],
        'industries': ['retail pharmacies', 'hospitals', 'clinics', 'pharmaceutical companies', 'research'],
        'description': "Pharmacists dispense prescription medications to patients and offer expertise in the safe use of prescriptions. They also may conduct health and wellness screenings, provide immunizations, oversee the medications given to patients, and provide advice on healthy lifestyles."
    },
    'Social Worker': {
        'skills': {'empathy': 0.9, 'communication': 0.9, 'problem-solving': 0.8, 'cultural competence': 0.8,
                   'case management': 0.7},
        'education': ['Social Work', 'Psychology', 'Sociology'],
        'work_style': ['office', 'field work', 'hybrid'],
        'industries': ['healthcare', 'mental health', 'schools', 'government', 'non-profit'],
        'description': "Social workers help people solve and cope with problems in their everyday lives. They work with diverse populations to provide resources, counseling, and support to improve their clients' well-being."
    },
    'Dentist': {
        'skills': {'dental procedures': 0.9, 'patient care': 0.9, 'dexterity': 0.8, 'diagnosis': 0.8,
                   'communication': 0.7},
        'education': ['Dentistry'],
        'work_style': ['on-site'],
        'industries': ['private practice', 'hospitals', 'public health', 'research', 'education'],
        'description': "Dentists diagnose and treat problems with patients' teeth, gums, and related parts of the mouth. They provide advice and instruction on taking care of teeth and gums and on diet choices that affect oral health."
    },
    'Business Analyst': {
        'skills': {'data analysis': 0.9, 'problem-solving': 0.8, 'communication': 0.8, 'project management': 0.7,
                   'business acumen': 0.8},
        'education': ['Business Administration', 'Information Systems', 'Economics'],
        'work_style': ['office', 'remote', 'hybrid'],
        'industries': ['consulting', 'finance', 'tech', 'healthcare', 'retail'],
        'description': "Business analysts help organizations improve their processes, products, services, and software through data analysis. They are responsible for bridging the gap between IT and the business using data analytics to assess processes, determine requirements and deliver data-driven recommendations and reports to executives and stakeholders."
    },
    'Pilot': {
        'skills': {'aircraft operation': 0.9, 'navigation': 0.9, 'decision making': 0.8, 'communication': 0.8,
                   'situational awareness': 0.9},
        'education': ['Aviation', 'Aeronautical Science'],
        'work_style': ['on-site', 'travel'],
        'industries': ['airlines', 'military', 'private aviation', 'cargo transportation', 'emergency services'],
        'description': "Pilots fly and navigate airplanes, helicopters, and other aircraft. They ensure the safe operation of aircraft and the safety of passengers and cargo. Airline pilots fly for airlines that transport people and cargo on a fixed schedule. Commercial pilots fly aircraft for other purposes, such as charter flights, rescue operations, firefighting, aerial photography, and crop dusting."
    },
    'Lawyer': {
        'skills': {'legal research': 0.9, 'critical thinking': 0.9, 'negotiation': 0.8, 'writing': 0.8,
                   'public speaking': 0.8},
        'education': ['Law'],
        'work_style': ['office', 'court', 'hybrid'],
        'industries': ['law firms', 'corporate', 'government', 'non-profit', 'private practice'],
        'description': "Lawyers advise and represent individuals, businesses, and government agencies on legal issues and disputes. They conduct research and analysis of legal problems, interpret laws, rulings and regulations for individuals and businesses. Lawyers also represent clients in court, at arbitrations, or in mediations."
    },
    'Data Analyst': {
        'skills': {'data analysis': 0.9, 'statistics': 0.8, 'programming': 0.7, 'data visualization': 0.8,
                   'problem-solving': 0.8},
        'education': ['Statistics', 'Mathematics', 'Computer Science', 'Economics'],
        'work_style': ['office', 'remote', 'hybrid'],
        'industries': ['tech', 'finance', 'healthcare', 'retail', 'consulting'],
        'description': "Data analysts collect, process, and perform statistical analyses of data. They help companies make better business decisions by identifying and analyzing trends and patterns in complex datasets. Their insights can help companies improve their products, services, and overall operations."
    },
    'Electrical Engineer': {
        'skills': {'circuit design': 0.9, 'problem-solving': 0.8, 'mathematics': 0.8, 'project management': 0.7,
                   'computer-aided design': 0.8},
        'education': ['Electrical Engineering', 'Electronics Engineering'],
        'work_style': ['office', 'field work', 'hybrid'],
        'industries': ['manufacturing', 'tech', 'aerospace', 'automotive', 'energy'],
        'description': "Electrical engineers design, develop, test, and supervise the manufacture of electrical equipment. This can include electric motors, radar and navigation systems, communications systems, and power generation equipment. They work on a variety of projects, from designing household appliances to developing telecommunications systems."
    },
    'Physical Education Teacher': {
        'skills': {'instruction': 0.9, 'physical fitness': 0.9, 'communication': 0.8, 'motivation': 0.8,
                   'first aid': 0.7},
        'education': ['Physical Education', 'Sports Science', 'Education'],
        'work_style': ['on-site'],
        'industries': ['education', 'sports', 'recreation', 'fitness centers', 'community programs'],
        'description': "Physical education teachers instruct students about sports, physical development, health, and proper nutrition. They organize games and challenges that promote physical activity among children and young adults in schools. They also focus on developing teamwork and leadership skills in their students."
    },
    'Biologist': {
        'skills': {'research': 0.9, 'data analysis': 0.8, 'laboratory techniques': 0.8, 'scientific writing': 0.7,
                   'critical thinking': 0.8},
        'education': ['Biology', 'Microbiology', 'Ecology', 'Genetics'],
        'work_style': ['laboratory', 'field work', 'office'],
        'industries': ['research institutions', 'pharmaceuticals', 'environmental agencies', 'biotechnology',
                       'education'],
        'description': "Biologists study living organisms and their relationship to the environment. They research how living systems work, how they evolve, and how biological processes can be harnessed for commercial or medical applications. They may specialize in a particular area such as marine biology, genetics, or ecology."
    },
    'Airline Flight Attendant': {
        'skills': {'customer service': 0.9, 'safety procedures': 0.9, 'communication': 0.8, 'problem-solving': 0.7,
                   'cultural awareness': 0.8},
        'education': ['High School Diploma', 'Hospitality', 'Tourism'],
        'work_style': ['travel', 'on-site'],
        'industries': ['airlines', 'aviation', 'travel', 'hospitality'],
        'description': "Flight attendants ensure the safety and comfort of airline passengers. They greet passengers, serve food and beverages, and assist with emergencies. They also provide information about the flight, ensure that safety regulations are followed, and assist passengers with special needs."
    },
    'Translator': {
        'skills': {'language proficiency': 0.9, 'writing': 0.8, 'cultural knowledge': 0.8, 'research': 0.7,
                   'attention to detail': 0.9},
        'education': ['Linguistics', 'Foreign Languages', 'Translation Studies'],
        'work_style': ['remote', 'office', 'freelance'],
        'industries': ['publishing', 'government', 'international organizations', 'media', 'business services'],
        'description': "Translators convert written material from one language into another. They must have excellent writing and analytical ability, and because the translations that they produce must be accurate, they also need good editing skills. Translators typically work on a variety of content, including legal documents, technical manuals, marketing materials, and literary works."
    },
    'Web Developer': {
        'skills': {'programming': 0.9, 'web technologies': 0.9, 'problem-solving': 0.8, 'design principles': 0.7,
                   'version control': 0.8},
        'education': ['Computer Science', 'Web Development', 'Information Technology'],
        'work_style': ['remote', 'office', 'hybrid'],
        'industries': ['tech', 'e-commerce', 'digital agencies', 'startups', 'consulting'],
        'description': "Web developers design and create websites. They are responsible for the look of the site as well as its technical aspects, such as performance and capacity. Web developers may also create site content that requires technical features. They work closely with clients and other team members to develop website specifications and functionality."
    },
    'Occupational Therapist': {
        'skills': {'patient care': 0.9, 'assessment': 0.8, 'treatment planning': 0.8, 'communication': 0.9,
                   'adaptability': 0.8},
        'education': ['Occupational Therapy'],
        'work_style': ['on-site', 'home visits'],
        'industries': ['healthcare', 'rehabilitation centers', 'schools', 'nursing homes', 'home health services'],
        'description': "Occupational therapists help patients develop, recover, improve, and maintain the skills needed for daily living and working. They work with patients who have injuries, illnesses, or disabilities, using everyday activities as therapy to help them lead independent, productive, and satisfying lives."
    }
}
