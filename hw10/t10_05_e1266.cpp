#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

int best_sum = 0;


void backtrack(const vector<int>& tracks, int index, int current_sum, int N) {
    if (current_sum > N) return;

    best_sum = max(best_sum, current_sum);

    for (size_t i = index; i < tracks.size(); i++) {
        backtrack(tracks, i + 1, current_sum + tracks[i], N);
    }
}

void find_best_tape_recording(int N, vector<int>& tracks) {
    best_sum = 0;
    backtrack(tracks, 0, 0, N);
    cout << "sum:" << best_sum << endl;
}

int main() {
    string line;


    while (getline(cin, line)) {
        stringstream ss(line);
        int N, s, duration;
        ss >> N >> s;

        vector<int> tracks;
        while (ss >> duration) {
            tracks.push_back(duration);
        }

        find_best_tape_recording(N, tracks);
    }

    return 0;
}

