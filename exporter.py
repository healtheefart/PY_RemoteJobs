import csv

def save_to_file(jobs_list, search_language):
  file = open(f"{search_language}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["title","company","link"])
  for job in jobs_list:
    writer.writerow(list(job.values()))
  return