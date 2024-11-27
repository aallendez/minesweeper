import csv
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


class LeaderboardWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        # Header Label
        header_label = QLabel("Top 10 Leaderboard")
        header_label.setFont(QFont("Arial", 24, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(header_label)

        self.leaderboard_file = "leaderboard.csv"
        self.load_and_display_leaderboard()

        self.setLayout(self.layout)

    def load_and_display_leaderboard(self):
        """
        Reads the leaderboard data from the CSV, sorts it, and displays the top 10 scores.
        """
        
        # Clear existing labels
        while self.layout.count() > 1:
            widget = self.layout.takeAt(1).widget()
            if widget:
                widget.deleteLater()

        # Read data from CSV
        leaderboard_data = self.read_leaderboard_csv()  # Read the leaderboard data

        # Sort data using MergeSort
        leaderboard_data = self.merge_sort(leaderboard_data, 1)  # Sort by time (index 1)

        # Display only the top 10 scores
        for index, player_data in enumerate(leaderboard_data[:10]):
            nickname, time = player_data
            
            # Format time to minutes:seconds if greater than 59
            formatted_time = self.format_time(time)
            
            player_label = QLabel(f"{index + 1}. {nickname}: {formatted_time}")
            player_label.setAlignment(Qt.AlignCenter)
            color = "#4DAA4D" if index % 2 == 0 else "#77C877"  # Alternate darker colors
            
            # Set style with bold font and larger text size
            player_label.setStyleSheet(f"background-color: {color}; padding: 5px; margin: 2px; border-radius: 5px; font-size: 18px; font-weight: bold;")
            self.layout.addWidget(player_label)

    def read_leaderboard_csv(self):
        """
        Reads leaderboard data from a CSV file.
        Returns a list of tuples [(nickname, time), ...].
        """
        leaderboard_data = []
        try:
            with open(self.leaderboard_file, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    nickname, time = row[0], int(row[1])  # Ensure time is an integer
                    leaderboard_data.append((nickname, time))
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            print("Leaderboard file not found. Creating a new one.")
        return leaderboard_data

    def write_to_leaderboard_csv(self, nickname, time):
        """
        Appends a new entry to the leaderboard CSV file.
        """
        with open(self.leaderboard_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([nickname, time])

    def quick_sort(self, data, low, high):
        """
        Implements QuickSort algorithm to sort leaderboard data by time.
        """
        if low < high:
            pivot_index = self.partition(data, low, high)
            self.quick_sort(data, low, pivot_index - 1)
            self.quick_sort(data, pivot_index + 1, high)

    def partition(self, data, low, high):
        """
        Helper function for QuickSort: partitions the data around a pivot.
        """
        pivot = data[high][1]  # Use the time as the pivot
        i = low - 1
        for j in range(low, high):
            if data[j][1] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1
    
    def merge_sort(self, data, index):
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = self.merge_sort(data[:mid], index)
        right = self.merge_sort(data[mid:], index)
        
        return self.merge(left, right, index)

    def merge(self, left, right, index):
        sorted_list = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i][index] < right[j][index]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
                
        while i < len(left):
            sorted_list.append(left[i])
            i += 1
            
        while j < len(right):
            sorted_list.append(right[j])
            j += 1
            
        return sorted_list

    def format_time(self, seconds):
        """Format time in seconds to 'minutes:seconds'."""
        if seconds >= 60:
            minutes = seconds // 60
            seconds = seconds % 60
            return f"{minutes}min {seconds:02d}s"
        return f"{seconds}s"
