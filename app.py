import streamlit as st

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Student Dashboard",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.dashboard-title {
    font-size: 38px;
    font-weight: 700;
    margin-bottom: 0;
}

.subtitle {
    font-size: 17px;
    opacity: 0.7;
    margin-bottom: 25px;
}

.card {
    padding: 20px;
    border-radius: 15px;
    border: 1px solid rgba(128,128,128,0.25);
    margin-bottom: 15px;
}

.card-title {
    font-size: 15px;
    opacity: 0.7;
}

.card-value {
    font-size: 30px;
    font-weight: 700;
    margin-top: 5px;
}

.section-title {
    font-size: 24px;
    font-weight: 650;
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ----------------
st.sidebar.title("🎓 Student Dashboard")
st.sidebar.caption("Your academic companion")

page = st.sidebar.selectbox(
    "Navigate",
    [
        "🏠 Home",
        "📌 Tasks",
        "📊 Marks",
        "📝 Assignments",
        "ℹ️ About"
    ]
)

st.sidebar.divider()

st.sidebar.info(
    "💡 Stay consistent.\n\n"
    "Small progress every day leads to big results."
)


# ==========================================================
# HOME
# ==========================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="dashboard-title">🎓 Student Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Track your academics, tasks and progress in one place.</div>',
        unsafe_allow_html=True
    )

    # Student name
    name = st.text_input(
        "👤 Student Name",
        placeholder="Enter your name"
    )

    if name:
        st.success(f"Welcome back, {name}! 👋")

    # ---------------- STATISTICS ----------------

    st.markdown(
        '<div class="section-title">📊 Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">📚 Subjects</div>
            <div class="card-value">6</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">📝 Assignments</div>
            <div class="card-value">4</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-title">✅ Completed</div>
            <div class="card-value">2</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="card-title">📈 Attendance</div>
            <div class="card-value">84%</div>
        </div>
        """, unsafe_allow_html=True)

    # ---------------- ATTENDANCE ----------------

    st.markdown(
        '<div class="section-title">📅 Attendance</div>',
        unsafe_allow_html=True
    )

    attendance_col1, attendance_col2 = st.columns([2, 1])

    with attendance_col1:

        st.write("Overall Attendance")

        st.progress(0.84)

        st.caption("84% attendance")

    with attendance_col2:

        st.metric(
            "Present",
            "42 / 50"
        )

    # ---------------- SUBJECT PROGRESS ----------------

    st.markdown(
        '<div class="section-title">📚 Subject Progress</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.write("🐍 Python")
        st.progress(0.85)
        st.caption("85% completed")

        st.write("📐 Mathematics")
        st.progress(0.70)
        st.caption("70% completed")

        st.write("🧪 Chemistry")
        st.progress(0.65)
        st.caption("65% completed")

    with col2:

        st.write("⚡ Physics")
        st.progress(0.60)
        st.caption("60% completed")

        st.write("💻 Programming")
        st.progress(0.80)
        st.caption("80% completed")

        st.write("📊 Data Science")
        st.progress(0.55)
        st.caption("55% completed")

    # ---------------- UPCOMING ----------------

    st.markdown(
        '<div class="section-title">📝 Upcoming Assignments</div>',
        unsafe_allow_html=True
    )

    assignment_col1, assignment_col2 = st.columns(2)

    with assignment_col1:

        st.info(
            "🐍 **Python Project**\n\n"
            "Due: Tomorrow"
        )

        st.warning(
            "📐 **Mathematics Assignment**\n\n"
            "Due: 3 days"
        )

    with assignment_col2:

        st.info(
            "🧪 **Chemistry Report**\n\n"
            "Due: 5 days"
        )

        st.success(
            "✅ **Physics Worksheet**\n\n"
            "Completed"
        )

    # ---------------- QUICK ACTIONS ----------------

    st.markdown(
        '<div class="section-title">⚡ Quick Actions</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📝 View Assignments", use_container_width=True):
            st.info("Use the Assignments page from the sidebar.")

    with col2:
        if st.button("📊 Check Marks", use_container_width=True):
            st.info("Use the Marks page from the sidebar.")

    with col3:
        if st.button("📌 View Tasks", use_container_width=True):
            st.info("Use the Tasks page from the sidebar.")


# ==========================================================
# TASKS
# ==========================================================

elif page == "📌 Tasks":

    st.title("📌 My Tasks")

    st.write("Complete your daily tasks:")

    task1 = st.checkbox("🐍 Complete Python practice")
    task2 = st.checkbox("📐 Revise Mathematics")
    task3 = st.checkbox("💻 Work on project")
    task4 = st.checkbox("📚 Read today's notes")

    completed = sum([task1, task2, task3, task4])

    st.divider()

    st.write(f"### Completed: {completed}/4")

    st.progress(completed / 4)

    if completed == 4:
        st.balloons()
        st.success("🎉 All tasks completed!")

    elif completed > 0:
        st.info("💪 Good progress! Keep going.")


# ==========================================================
# MARKS
# ==========================================================

elif page == "📊 Marks":

    st.title("📊 Marks & Grades")

    st.write("Enter your marks out of 100.")

    maths = st.number_input(
        "📐 Mathematics",
        min_value=0,
        max_value=100,
        value=0
    )

    python = st.number_input(
        "🐍 Python",
        min_value=0,
        max_value=100,
        value=0
    )

    chemistry = st.number_input(
        "🧪 Chemistry",
        min_value=0,
        max_value=100,
        value=0
    )

    physics = st.number_input(
        "⚡ Physics",
        min_value=0,
        max_value=100,
        value=0
    )

    if st.button("Calculate Result"):

        average = (maths + python + chemistry + physics) / 4

        st.divider()

        st.subheader("📋 Your Result")

        st.metric(
            "📈 Average Marks",
            f"{average:.2f}%"
        )

        if average >= 90:
            st.success("🏆 Excellent!")

        elif average >= 75:
            st.success("🌟 Very Good!")

        elif average >= 60:
            st.info("👍 Good!")

        elif average >= 40:
            st.warning("📚 Keep studying!")

        else:
            st.error("⚠️ You need more practice.")


# ==========================================================
# ASSIGNMENTS
# ==========================================================

elif page == "📝 Assignments":

    st.title("📝 Assignment Tracker")

    st.write("Add and track your assignments.")

    assignment = st.text_input(
        "📌 Assignment name"
    )

    subject = st.selectbox(
        "📚 Subject",
        [
            "Python",
            "Mathematics",
            "Physics",
            "Chemistry",
            "Other"
        ]
    )

    due_date = st.date_input(
        "📅 Due date"
    )

    completed = st.checkbox(
        "✅ Assignment completed"
    )

    if st.button("Add Assignment"):

        if assignment:

            st.success(
                f"Added: {assignment} | "
                f"Subject: {subject} | "
                f"Due: {due_date}"
            )

            if completed:
                st.info("Status: Completed ✅")

            else:
                st.warning("Status: Pending ⏳")

        else:

            st.error(
                "Please enter an assignment name."
            )


# ==========================================================
# ABOUT
# ==========================================================

elif page == "ℹ️ About":

    st.title("ℹ️ About")

    st.write(
        "This is a Student Dashboard created using Streamlit."
    )

    st.write(
        "It helps students track attendance, "
        "tasks, marks and assignments."
    )

    st.divider()

    st.subheader("🎯 Goal")

    st.write(
        "To provide students with a simple and "
        "organized way to manage their academic progress."
    )

    st.success(
        "🎓 Keep learning and keep improving!"
    )