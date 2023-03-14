# Approach 1
# O(N*M)+O(N * LogN), O(M) - M is max_deadline
def JobScheduling(self,Jobs,n):
    # Sort based on profit
    jobs = sorted(Jobs, reverse=True, key=lambda x: x.profit)

    # Find max deadline
    max_deadline = max([job.deadline for job in Jobs])
    timeline = [-1]*max_deadline

    # Calculate
    num_jobs, max_profit = 0, 0
    for job in jobs:
        i = job.deadline-1
        while i>=0 and timeline[i] != -1:
            i-=1
        if i >= 0:
            timeline[i] = 1
            num_jobs += 1
            max_profit += job.profit
    return [num_jobs, max_profit]

# Approach 1 in C++
# The same approach as above, but in C++ it is accepted
# bool static comparison(Job a, Job b) {
#          return (a.profit > b.profit);
#       }

#     vector<int> JobScheduling(Job arr[], int n)
#     {
#         sort(arr, arr + n, comparison);
#         int maxi = arr[0].dead;
#         for (int i = 1; i < n; i++) {
#          maxi = max(maxi, arr[i].dead);
#         }

#         int slot[maxi + 1];

#         for (int i = 0; i <= maxi; i++)
#          slot[i] = -1;

#         int countJobs = 0, jobProfit = 0;

#         for (int i = 0; i < n; i++) {
#          for (int j = arr[i].dead; j > 0; j--) {
#             if (slot[j] == -1) {
#                slot[j] = i;
#                countJobs++;
#                jobProfit += arr[i].profit;
#                break;
#             }
#          }
#         }

#         vector<int> res;
#         res.push_back(countJobs);
#         res.push_back(jobProfit);
#         return res;
#     }