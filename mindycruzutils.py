# Mindy Cruz
# P1  Create a New Python Module

#1. Project Start
'''This module provides a reusable byline for the author's services. '''

#2. Import dependencies
import math
import statistics

#3. Define variables

company_name: str = "Greninja Analytics LLC"
company_established: int = "2004"
location: str = "Topeka, KS"
internationally_known: bool = True
feedback_score: float = 8.9
employee_count: int = 3
services: list = ['Industry Comparison', 'Performance Audit', 'Improvement Review']
service_cost: list = [2500, 3500, 5000]

#4. Fstring

company_name: str = f"Company: {company_name}"
location: str = f"Location: {location}"
company_established: int = f"Company Established: {company_established}"
internationally_known: bool = f"International Exposure: {internationally_known}"    
employee_count: int = f"Employees on Staff: {employee_count}"
services: list = f"Available Services: {services}"
feedback_score: float = f"Average Customer Feedback: {feedback_score}"


#5. Calculate Descriptive Stats

smallest= min(service_cost)
largest= max(service_cost)
total= sum(service_cost)
count= len(service_cost)
mean= statistics.mean(service_cost)
mode= statistics.mode(service_cost)
median= statistics.median(service_cost)
standard_deviation=statistics.stdev(service_cost)

stats_string = f"""
Average Service Cost:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""
#6. Byline String

byline = f"""
Company Details:
{company_name}
{location}
{company_established}
{feedback_score}
 
Service Details:
{services}
Cost: {service_cost}
{feedback_score}
Median Cost: {median}
Cheapest 
"""
#7. Define Main Function

def main():
    print(company_name)
    print(location)
    print(company_established)
    print(internationally_known)
    print(feedback_score)
    print(employee_count)
    print(byline)

#8 Function Call

if __name__ == "__main__":
    main()
