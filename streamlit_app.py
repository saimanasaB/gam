import streamlit as st

class JobNode:
    def __init__(self, level, profit, bound, job):
        self.level = level
        self.profit = profit
        self.bound = bound
        self.job = job

def calculate_bound(u, n, deadline, jobs):
    if u.level == n:
        return 0

    j = u.level + 1
    bound = u.profit
    weight = 0

    while j < n and weight + jobs[j][2] <= deadline:
        weight += jobs[j][2]
        bound += jobs[j][2]
        j += 1

    if j < n:
        bound += (deadline - weight) * jobs[j][2] / jobs[j][1]

    return bound

def job_sequencing_branch_and_bound(jobs, deadline):
    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort by profit in descending order
    n = len(jobs)
    max_profit = 0
    queue = []

    u = JobNode(-1, 0, 0, None)
    v = JobNode(-1, 0, 0, None)

    queue.append(u)

    while queue:
        u = queue.pop(0)

        if u.level == -1:
            v.level = 0

        if u.level == n - 1:
            continue

        v.level = u.level + 1
        v.profit = u.profit + jobs[v.level][2]
        v.bound = calculate_bound(v, n, deadline, jobs)

        if v.profit > max_profit:
            max_profit = v.profit

        if v.bound > max_profit:
            queue.append(v)

        v.profit = u.profit
        v.bound = calculate_bound(v, n, deadline, jobs)

        if v.bound > max_profit:
            queue.append(v)

    return max_profit

def main():
    st.title("Job Sequencing Problem Solver")

    num_jobs = st.number_input("Enter number of jobs", min_value=1, step=1, value=1)

    jobs = []
    max_deadline = 0

    for i in range(num_jobs):
        job_id = st.text_input(f"Job {i+1} ID")
        deadline = st.number_input(f"Job {i+1} Deadline", min_value=1, step=1)
        profit = st.number_input(f"Job {i+1} Profit", min_value=0, step=1)
        jobs.append((job_id, deadline, profit))
        max_deadline = max(max_deadline, deadline)

    if st.button("Solve"):
        total_profit = job_sequencing_branch_and_bound(jobs, max_deadline)
        st.write("Branch and Bound Method:")
        st.write("Total Profit:", total_profit)

if __name__ == "__main__":
    main()
