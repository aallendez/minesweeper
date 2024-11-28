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
        Time Complexity: O(n log n) for merge sort, O(n) for displaying top 10.
        """
        
        # Clear existing labels
        while self.layout.count() > 1:  # O(n) for clearing labels
            widget = self.layout.takeAt(1).widget()
            if widget:
                widget.deleteLater()

        # Read data from CSV
        leaderboard_data = self.read_leaderboard_csv()  # O(n)

        # Sort data using MergeSort
        leaderboard_data = self.merge_sort(leaderboard_data, 1)  # O(n log n)

        # Display only the top 10 scores
        for index, player_data in enumerate(leaderboard_data[:10]):  # O(10) = O(1)
            nickname, time = player_data
            
            # Format time to minutes:seconds if greater than 59
            formatted_time = self.format_time(time)  # O(1)
            
            player_label = QLabel(f"{index + 1}. {nickname}: {formatted_time}")  # O(1)
            player_label.setAlignment(Qt.AlignCenter)  # O(1)
            color = "#4DAA4D" if index % 2 == 0 else "#77C877"  # O(1)
            
            # Set style with bold font and larger text size
            player_label.setStyleSheet(f"background-color: {color}; padding: 5px; margin: 2px; border-radius: 5px; font-size: 18px; font-weight: bold;")  # O(1)
            self.layout.addWidget(player_label)  # O(1)

    def read_leaderboard_csv(self):
        """
        Reads leaderboard data from a CSV file.
        Returns a list of tuples [(nickname, time), ...].
        Time Complexity: O(n)
        """
        leaderboard_data = []
        try:
            with open(self.leaderboard_file, "r") as file:  # O(1)
                reader = csv.reader(file)  # O(1)
                for row in reader:  # O(n)
                    nickname, time = row[0], int(row[1])  # O(1)
                    leaderboard_data.append((nickname, time))  # O(1)
        except FileNotFoundError:
            # If the file doesn't exist, return an empty list
            print("Leaderboard file not found. Creating a new one.")  # O(1)
        return leaderboard_data  # O(1)

    def write_to_leaderboard_csv(self, nickname, time):
        """
        Appends a new entry to the leaderboard CSV file.
        Best Case: O(1) - New entry is added to the leaderboard
        Average Case: O(1) - New entry is added to the leaderboard
        Worst Case: O(1) - New entry is added to the leaderboard
        """
        with open(self.leaderboard_file, "a", newline="") as file:  # O(1)
            writer = csv.writer(file)  # O(1)
            writer.writerow([nickname, time])  # O(1)

    def merge_sort(self, data, index):
        """
        Sorts the data using the Merge Sort algorithm.

        Time Complexity Analysis:
        - Merge Sort divides the list into two halves recursively, sorts each half, and then merges them.
        - The splitting operation occurs log(n) times (dividing the data into halves).
        - The merging operation, which is linear (O(n)), happens at each level of recursion.
        - Therefore, the total complexity is O(n log n).

        Best Case: O(n log n)
        - Even if the data is already sorted, the recursive splitting and merging steps still occur.

        Average Case: O(n log n)
        - The general case where data requires sorting during merge operations.

        Worst Case: O(n log n)
        - Even in the worst case (completely unsorted data), the complexity remains O(n log n) 
        because all elements are processed and merged at every level.

        Space Complexity:
        - Merge Sort requires O(n) auxiliary space for the merged array, making it less space-efficient than in-place sorting algorithms.

        Why Merge Sort is the best option for this task:
        1. Stable Sorting: Merge Sort maintains the relative order of equal elements, which is essential for sorting by one key (e.g., `index`) while preserving existing order from prior sorts.
        2. Predictable Performance: Unlike QuickSort, which can degrade to O(n^2) in the worst case, Merge Sort consistently performs at O(n log n) regardless of the input distribution. It is convenient to do this if we plan the game to scale.
        3. Handles Large Data Efficiently: Merge Sort processes large datasets effectively, especially when data is stored in linked lists or external storage, as it works well with sequential access patterns.
        4. Ease of Implementation for Recursive Structures: The divide-and-conquer approach naturally fits recursive programming, making it straightforward to implement and debug.

        Why not QuickSort or other algorithms?
        - QuickSort has a lower average constant factor for in-place operations, but its worst-case performance (O(n^2)) makes it unsuitable for guaranteed efficiency.
        - Bubble Sort is too slow for large datasets, with O(n^2) time complexity in most cases.
        """
        if len(data) <= 1:  # Base case: lists of size 1 or empty are already sorted. O(1)
            return data  # O(1)
        
        mid = len(data) // 2  # Find the midpoint of the list. O(1)
        # Recursively sort the left and right halves. Each call is O(n log n).
        left = self.merge_sort(data[:mid], index)
        right = self.merge_sort(data[mid:], index)
        
        # Merge the two sorted halves. O(n)
        return self.merge(left, right, index)

    def merge(self, left, right, index):
        """
        Merges two sorted lists into a single sorted list.

        Time Complexity Analysis:
        - The merge function processes all elements in `left` and `right` exactly once.
        - Therefore, the time complexity is O(n), where n = len(left) + len(right).

        Best Case: O(n)
        - All elements in `left` and `right` are processed in a single pass.

        Average Case: O(n)
        - On average, every element in `left` and `right` is compared once and added to the result.

        Worst Case: O(n)
        - Regardless of the input distribution, every element in both lists must be processed.

        Space Complexity:
        - Requires additional space for the merged list, proportional to the total size of `left` and `right`.
        """
        sorted_list = []  # Initialize an empty list for the sorted result. O(1)
        i = j = 0  # Indices for iterating over `left` and `right`. O(1)
        
        # Process both lists until one is exhausted. O(n)
        while i < len(left) and j < len(right):  
            if left[i][index] < right[j][index]:  # Compare elements at the given index. O(1)
                sorted_list.append(left[i])  # Append smaller element to the result. O(1)
                i += 1  # Move to the next element in `left`. O(1)
            else:
                sorted_list.append(right[j])  # Append smaller element to the result. O(1)
                j += 1  # Move to the next element in `right`. O(1)
        
        # Append any remaining elements from `left`. O(n)
        while i < len(left):
            sorted_list.append(left[i])
            i += 1
        
        # Append any remaining elements from `right`. O(n)
        while j < len(right):
            sorted_list.append(right[j])
            j += 1
        
        return sorted_list  # Return the merged and sorted list. O(1)


    def format_time(self, seconds):
        """Format time in seconds to 'minutes:seconds'.
        Time Complexity: O(1)
        """
        if seconds >= 60:  # O(1)
            minutes = seconds // 60  # O(1)
            seconds = seconds % 60  # O(1)
            return f"{minutes}min {seconds:02d}s"  # O(1)
        return f"{seconds}s"  # O(1)

    # Decided to implement merge sort instead of quick sort, this is just for visibility
    def quick_sort(self, data, low, high):
        """
        Implements QuickSort algorithm to sort leaderboard data by time.
        """
        if low < high:
            pivot_index = self.partition(data, low, high)
            self.quick_sort(data, low, pivot_index - 1)
            self.quick_sort(data, pivot_index + 1, high)

    # Decided to implement merge sort instead of quick sort, this is just for visibility
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
    