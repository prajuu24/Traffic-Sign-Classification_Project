import matplotlib.pyplot as plt
import numpy as np

# Assuming you have precision, recall, f1_score, and classes defined
# Replace these arrays with your actual data
precision = [0.98, 1.00, 0.97, 0.97, 0.99, 0.97, 0.97, 1.00, 0.97, 1.00, 
              0.98, 0.99, 1.00, 1.00, 1.00, 1.00, 0.89, 1.00, 0.99, 0.99, 
              1.00, 0.99, 1.00, 0.96, 1.00, 0.98, 0.97, 1.00, 0.99, 1.00, 
              0.99, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.99, 1.00, 0.99, 
              0.98, 0.98, 1.00, 0.98, 1.00, 1.00, 1.00, 1.00]  # List of precision values
recall = [0.98, 0.97, 0.99, 1.00, 0.99, 0.98, 1.00, 0.95, 1.00, 0.93, 
           1.00, 0.99, 1.00, 1.00, 1.00, 0.99, 1.00, 1.00, 1.00, 0.99, 
           0.99, 1.00, 0.95, 1.00, 0.96, 0.94, 0.97, 1.00, 0.94, 0.99, 
           1.00, 1.00, 1.00, 1.00, 1.00, 0.99, 1.00, 1.00, 1.00, 0.99, 
           1.00, 1.00, 0.99, 1.00, 1.00, 0.87, 0.99, 0.94]     # List of recall values
f1_score = [0.98, 0.98, 0.98, 0.98, 0.99, 0.98, 0.99, 0.97, 0.98, 0.96, 
             0.99, 0.99, 1.00, 1.00, 1.00, 1.00, 0.94, 0.99, 0.99, 0.99, 
             0.99, 0.99, 0.98, 0.97, 1.00, 0.98, 0.95, 0.98, 0.98, 0.98, 
             0.99, 0.99, 1.00, 0.99, 1.00, 1.00, 1.00, 1.00, 1.00, 0.99, 
             1.00, 1.00, 1.00, 1.00, 0.93, 0.99, 0.99]  # List of F1-score values
classes = list(range(1, len(precision) + 1))  # List of class numbers

# Ensure that precision, recall, and f1_score have the same length
min_length = min(len(precision), len(recall), len(f1_score))
precision = precision[:min_length]
recall = recall[:min_length]
f1_score = f1_score[:min_length]
classes = classes[:min_length]

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

# First subplot for the left half
bar_width = 0.25
opacity = 0.8
index = np.arange(len(classes))

rects1 = ax1.bar(index - bar_width, precision, bar_width, alpha=opacity, color='b', label='Precision')
rects2 = ax1.bar(index, recall, bar_width, alpha=opacity, color='g', label='Recall')
rects3 = ax1.bar(index + bar_width, f1_score, bar_width, alpha=opacity, color='r', label='F1-score')
ax1.set_xlabel('Classes', fontsize=14)
ax1.set_ylabel('Scores', fontsize=14)
ax1.set_title('Left Half: Precision, Recall, and F1-score for Each Class', fontsize=16)
ax1.set_xticks(index)
ax1.set_xticklabels(classes, fontsize=10)
ax1.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Adjust the legend position

# Second subplot for the right half
rects1 = ax2.bar(index - bar_width, precision, bar_width, alpha=opacity, color='b', label='Precision')
rects2 = ax2.bar(index, recall, bar_width, alpha=opacity, color='g', label='Recall')
rects3 = ax2.bar(index + bar_width, f1_score, bar_width, alpha=opacity, color='r', label='F1-score')
ax2.set_xlabel('Classes', fontsize=14)
ax2.set_ylabel('Scores', fontsize=14)
ax2.set_title('Right Half: Precision, Recall, and F1-score for Each Class', fontsize=16)
ax2.set_xticks(index)
ax2.set_xticklabels(classes, fontsize=10)
ax2.legend(loc='upper left', bbox_to_anchor=(1, 1))  # Adjust the legend position

plt.tight_layout()
plt.show()
