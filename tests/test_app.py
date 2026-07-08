from src import app as app_module


def test_github_skills_activity_is_available():
    assert "GitHub Skills" in app_module.activities

    activity = app_module.activities["GitHub Skills"]
    assert activity["description"] == "Learn practical coding and collaboration skills through GitHub"
    assert activity["schedule"] == "Wednesdays, 3:30 PM - 4:30 PM"
    assert activity["max_participants"] == 18
