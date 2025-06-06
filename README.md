### 📁 2. Directory Change Monitoring

**Objective:**
- Create a script that generates a "snapshot" of files in a directory (e.g., `/etc`), saving hashes and paths.
- On subsequent execution, compare the new snapshot with the previous one.
- Highlight modified, added, or removed files.

**✅ Success Criteria:**
- The script creates a snapshot file with file hashes.
- Compares two snapshots and shows differences.
- Highlights new, modified, or deleted files.

**💡 Extra Challenge:**
- Send a notification (e.g., email or Telegram message) if changes are detected.
- Integrate with `inotifywait` for real-time monitoring.
