# =========================================================
# NATIONAL PROGRAMME ANALYTICS DATASET GENERATOR
# OPTIMIZED FOR VS CODE / LOCAL MACHINE
# POWER BI FRIENDLY
# =========================================================

import pandas as pd
import numpy as np
import random
import uuid
import zipfile

from datetime import timedelta

# =========================================================
# INITIAL SETUP
# =========================================================

np.random.seed(42)
random.seed(42)

# =========================================================
# CONFIGURATION
# =========================================================

START_DATE = "2024-01-01"
END_DATE = "2025-12-31"

NUM_LEARNERS = 50000
NUM_PROGRAMMES = 450

# =========================================================
# PROGRAMME DEFINITIONS
# =========================================================

core_programmes = [
    "Data Analytics",
    "Web Development",
    "Cybersecurity",
    "Cloud Computing",
    "Product Design",
    "Digital Marketing",
    "AI Engineering"
]

masterclasses = [
    "CV Writing",
    "LinkedIn Optimisation",
    "Freelancing",
    "AI Productivity",
    "Career Readiness",
    "Remote Work Essentials"
]

orientation_sessions = [
    "Programme Orientation",
    "Platform Walkthrough",
    "Mentor Introduction"
]

# =========================================================
# REGIONS & STATES
# =========================================================

regions = {
    "Lagos": "South West",
    "Oyo": "South West",
    "Ogun": "South West",
    "Osun": "South West",
    "Ondo": "South West",

    "Rivers": "South South",
    "Delta": "South South",
    "Edo": "South South",
    "Akwa Ibom": "South South",
    "Bayelsa": "South South",

    "Enugu": "South East",
    "Anambra": "South East",
    "Imo": "South East",
    "Abia": "South East",
    "Ebonyi": "South East",

    "Kaduna": "North West",
    "Kano": "North West",
    "Katsina": "North West",
    "Sokoto": "North West",
    "Jigawa": "North West",

    "FCT": "North Central",
    "Benue": "North Central",
    "Plateau": "North Central",
    "Niger": "North Central",
    "Kogi": "North Central",

    "Borno": "North East",
    "Adamawa": "North East",
    "Bauchi": "North East",
    "Taraba": "North East",
    "Yobe": "North East"
}

# =========================================================
# REALISTIC STATE WEIGHTS
# =========================================================

state_weights = {
    "Lagos": 0.12,
    "Oyo": 0.05,
    "Ogun": 0.04,
    "Osun": 0.03,
    "Ondo": 0.03,

    "Rivers": 0.06,
    "Delta": 0.05,
    "Edo": 0.04,
    "Akwa Ibom": 0.03,
    "Bayelsa": 0.02,

    "Enugu": 0.04,
    "Anambra": 0.05,
    "Imo": 0.03,
    "Abia": 0.03,
    "Ebonyi": 0.02,

    "Kaduna": 0.06,
    "Kano": 0.08,
    "Katsina": 0.04,
    "Sokoto": 0.03,
    "Jigawa": 0.03,

    "FCT": 0.07,
    "Benue": 0.03,
    "Plateau": 0.03,
    "Niger": 0.02,
    "Kogi": 0.02,

    "Borno": 0.015,
    "Adamawa": 0.02,
    "Bauchi": 0.025,
    "Taraba": 0.015,
    "Yobe": 0.015
}

states = list(state_weights.keys())

# NORMALIZE PROBABILITIES
total_weight = sum(state_weights.values())

state_probability = [
    weight / total_weight
    for weight in state_weights.values()
]

# =========================================================
# PROVIDERS
# =========================================================

providers = [
    "Tech4Dev",
    "Utiva",
    "Ingressive",
    "Decagon",
    "AltSchool",
    "DataCamp Africa",
    "TalentQL"
]

# =========================================================
# GENERATE LEARNERS TABLE
# =========================================================

print("Generating learners dataset...")

learners = pd.DataFrame({

    "learner_id": [
        f"LRN{i:07}"
        for i in range(NUM_LEARNERS)
    ],

    "gender": np.random.choice(
        ["Male", "Female"],
        NUM_LEARNERS,
        p=[0.52, 0.48]
    ),

    "age_group": np.random.choice(
        ["18-24", "25-34", "35-44"],
        NUM_LEARNERS,
        p=[0.55, 0.35, 0.10]
    ),

    "state_of_origin": np.random.choice(
        states,
        NUM_LEARNERS,
        p=state_probability
    ),

    "state_of_residence": np.random.choice(
        states,
        NUM_LEARNERS,
        p=state_probability
    ),

    "education_level": np.random.choice(
        [
            "Secondary School",
            "OND/ND",
            "Undergraduate",
            "Graduate",
            "Postgraduate"
        ],
        NUM_LEARNERS,
        p=[0.12, 0.18, 0.42, 0.22, 0.06]
    ),

    "employment_status": np.random.choice(
        [
            "Student",
            "Employed",
            "Self-Employed",
            "Unemployed"
        ],
        NUM_LEARNERS,
        p=[0.40, 0.25, 0.10, 0.25]
    ),

    "device_access": np.random.choice(
        ["Yes", "No"],
        NUM_LEARNERS,
        p=[0.92, 0.08]
    ),

    "primary_device": np.random.choice(
        [
            "Mobile Phone",
            "Laptop",
            "Tablet",
            "Desktop"
        ],
        NUM_LEARNERS,
        p=[0.55, 0.35, 0.05, 0.05]
    ),

    "prior_tech_experience": np.random.choice(
        ["Beginner", "Intermediate", "Advanced"],
        NUM_LEARNERS,
        p=[0.60, 0.30, 0.10]
    ),

    "monthly_income_band": np.random.choice(
        [
            "<50k",
            "50k-100k",
            "100k-250k",
            "250k+"
        ],
        NUM_LEARNERS,
        p=[0.40, 0.35, 0.20, 0.05]
    ),

    "registration_source": np.random.choice(
        [
            "Social Media",
            "Referral",
            "Email Campaign",
            "Campus Outreach",
            "Community Outreach",
            "Partner Organisation"
        ],
        NUM_LEARNERS,
        p=[0.35, 0.18, 0.12, 0.15, 0.10, 0.10]
    )
})

# =========================================================
# REGIONAL MAPPING
# =========================================================

learners["region_of_origin"] = learners[
    "state_of_origin"
].map(regions)

learners["region_of_residence"] = learners[
    "state_of_residence"
].map(regions)

# =========================================================
# INTERNET QUALITY VARIABILITY
# =========================================================

def assign_internet_quality(region):

    if region == "South West":

        return np.random.choice(
            ["Good", "Moderate", "Poor"],
            p=[0.60, 0.30, 0.10]
        )

    elif region == "North East":

        return np.random.choice(
            ["Good", "Moderate", "Poor"],
            p=[0.15, 0.45, 0.40]
        )

    elif region == "North West":

        return np.random.choice(
            ["Good", "Moderate", "Poor"],
            p=[0.25, 0.50, 0.25]
        )

    else:

        return np.random.choice(
            ["Good", "Moderate", "Poor"],
            p=[0.35, 0.45, 0.20]
        )

learners["internet_quality"] = learners[
    "region_of_residence"
].apply(assign_internet_quality)

# =========================================================
# PROGRAMMES TABLE
# =========================================================

print("Generating programmes dataset...")

programme_rows = []

date_range = pd.date_range(
    START_DATE,
    END_DATE
)

for i in range(NUM_PROGRAMMES):

    programme_type = np.random.choice(
        ["Core Programme", "Masterclass", "Orientation"],
        p=[0.35, 0.45, 0.20]
    )

    if programme_type == "Core Programme":

        programme_name = random.choice(
            core_programmes
        )

        duration = random.randint(45, 60)

        participants = random.randint(
            200,
            1200
        )

    elif programme_type == "Masterclass":

        programme_name = random.choice(
            masterclasses
        )

        duration = random.randint(3, 7)

        participants = random.randint(
            500,
            5000
        )

    else:

        programme_name = random.choice(
            orientation_sessions
        )

        duration = random.randint(1, 2)

        participants = random.randint(
            1000,
            8000
        )

    start_date = random.choice(date_range)

    end_date = start_date + timedelta(days=duration)

    programme_rows.append({

        "programme_id":
            f"PRG{i:05}",

        "programme_name":
            programme_name,

        "programme_type":
            programme_type,

        "provider":
            random.choice(providers),

        "start_date":
            start_date,

        "end_date":
            end_date,

        "duration_days":
            duration,

        "participants_target":
            participants
    })

programmes = pd.DataFrame(programme_rows)

# =========================================================
# OPTIMIZED LOOKUP
# =========================================================

learner_region_lookup = dict(
    zip(
        learners["learner_id"],
        learners["region_of_residence"]
    )
)

# =========================================================
# PARTICIPATION TABLE
# =========================================================

print("Generating participation records...")

participation_rows = []

for _, programme in programmes.iterrows():

    participant_count = programme[
        "participants_target"
    ]

    sampled_learners = learners.sample(
        min(participant_count, len(learners)),
        replace=False
    )

    for learner_id in sampled_learners[
        "learner_id"
    ]:

        learner_region = learner_region_lookup[
            learner_id
        ]

        # REGIONAL VARIABILITY

        if learner_region == "South West":

            engagement_base = 78
            dropout_modifier = 0.85

        elif learner_region == "North East":

            engagement_base = 58
            dropout_modifier = 1.35

        elif learner_region == "North West":

            engagement_base = 63
            dropout_modifier = 1.15

        else:

            engagement_base = 70
            dropout_modifier = 1.0

        engagement_score = np.random.normal(
            engagement_base,
            15
        )

        engagement_score = max(
            20,
            min(100, engagement_score)
        )

        attendance_rate = np.random.normal(
            engagement_base,
            18
        )

        attendance_rate = max(
            20,
            min(100, attendance_rate)
        )

        login_count = max(
            1,
            int(np.random.normal(18, 8))
        )

        assignments_completed = max(
            0,
            int(np.random.normal(5, 2))
        )

        quiz_score = max(
            20,
            min(
                100,
                np.random.normal(
                    engagement_base,
                    14
                )
            )
        )

        completed_prob = min(
            0.85,
            engagement_score / 100
        )

        dropped_prob = max(
            0.05,
            (
                0.30 -
                (engagement_score / 200)
            ) * dropout_modifier
        )

        ongoing_prob = 1 - (
            completed_prob +
            dropped_prob
        )

        if ongoing_prob < 0:
            ongoing_prob = 0.05

        total = (
            completed_prob +
            dropped_prob +
            ongoing_prob
        )

        completed_prob /= total
        dropped_prob /= total
        ongoing_prob /= total

        completion_status = np.random.choice(
            [
                "Completed",
                "Dropped",
                "Ongoing"
            ],
            p=[
                completed_prob,
                dropped_prob,
                ongoing_prob
            ]
        )

        if completion_status == "Dropped":

            dropout_reason = np.random.choice([
                "Internet Issues",
                "Financial Constraints",
                "Time Constraints",
                "Lost Interest",
                "Work Conflict",
                "Unknown"
            ])

        else:

            dropout_reason = None

        if engagement_score >= 75:

            risk_level = "Low"

        elif engagement_score >= 50:

            risk_level = "Medium"

        else:

            risk_level = "High"

        participation_rows.append({

            "participation_id":
                str(uuid.uuid4()),

            "learner_id":
                learner_id,

            "programme_id":
                programme["programme_id"],

            "programme_name":
                programme["programme_name"],

            "programme_type":
                programme["programme_type"],

            "provider":
                programme["provider"],

            "programme_start_date":
                programme["start_date"],

            "programme_end_date":
                programme["end_date"],

            "attendance_rate":
                round(attendance_rate, 1),

            "engagement_score":
                round(engagement_score, 1),

            "login_count":
                login_count,

            "assignments_completed":
                assignments_completed,

            "quiz_score":
                round(quiz_score, 1),

            "completion_status":
                completion_status,

            "dropout_reason":
                dropout_reason,

            "risk_level":
                risk_level
        })

participation = pd.DataFrame(
    participation_rows
)

# =========================================================
# DATE FEATURES
# =========================================================

participation["year"] = pd.to_datetime(
    participation["programme_start_date"]
).dt.year

participation["month"] = pd.to_datetime(
    participation["programme_start_date"]
).dt.month_name()

participation["month_number"] = pd.to_datetime(
    participation["programme_start_date"]
).dt.month

participation["quarter"] = pd.to_datetime(
    participation["programme_start_date"]
).dt.quarter

participation["week"] = pd.to_datetime(
    participation["programme_start_date"]
).dt.isocalendar().week

# =========================================================
# MERGE DATASETS
# =========================================================

print("Merging datasets...")

final_dataset = participation.merge(
    learners,
    on="learner_id",
    how="left"
)

# =========================================================
# SUMMARY
# =========================================================

print("\n==============================")
print("DATASET SUMMARY")
print("==============================")

print(
    f"\nTotal Learners: {len(learners):,}"
)

print(
    f"Total Programmes: {len(programmes):,}"
)

print(
    f"Total Participations: "
    f"{len(final_dataset):,}"
)

print("\nRegional Distribution:")
print(
    final_dataset["region_of_residence"]
    .value_counts()
)

# =========================================================
# EXPORT FILES
# =========================================================

print("\nExporting CSV files...")

learners.to_csv(
    "learners.csv",
    index=False
)

programmes.to_csv(
    "programmes.csv",
    index=False
)

final_dataset.to_csv(
    "programme_participation.csv",
    index=False
)

print("\nCSV export complete.")

# =========================================================
# CREATE ZIP
# =========================================================

print("\nCreating ZIP archive...")

with zipfile.ZipFile(
    "programme_analytics_dataset.zip",
    "w",
    zipfile.ZIP_DEFLATED
) as zipf:

    zipf.write("learners.csv")
    zipf.write("programmes.csv")
    zipf.write("programme_participation.csv")

print("\nZIP archive created.")

print("\nDONE!")