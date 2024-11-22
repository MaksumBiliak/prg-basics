
distances_traveled = [120, 150, 180, 90, 200, 175, 160]


sorted_distances = sorted(distances_traveled)
print("Distances traveled (sorted ascending):", sorted_distances)


daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]


sorted_temperatures = sorted(daily_temperatures, reverse=True)
print("Daily temperatures (sorted descending):", sorted_temperatures)

file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
              "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

sorted_files = sorted(file_names)
print("File names (sorted ascending):", sorted_files)
