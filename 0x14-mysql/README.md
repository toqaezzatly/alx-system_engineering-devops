What is the main role of a database?
The main role of a database is to store, organize, and manage data in a structured way, allowing for efficient data retrieval, insertion, updating, and deletion. Databases provide a systematic way to handle large amounts of data, support data integrity, and enable concurrent access by multiple users or applications.

What is a database replica?
A database replica is a copy of a database that is maintained and synchronized with the primary database. Replication ensures that the replica remains up-to-date with changes made to the primary database. Database replicas can be used for various purposes, including load balancing, disaster recovery, and data redundancy.

What is the purpose of a database replica?
The purpose of a database replica includes:

Load Balancing: Distributing read queries across multiple replicas to reduce the load on the primary database and improve performance.
Disaster Recovery: Providing a backup that can be used in case the primary database fails.
Data Redundancy: Ensuring that there are multiple copies of data available to prevent data loss.
Geographical Distribution: Providing data closer to users in different geographical locations for faster access.
Why database backups need to be stored in different physical locations?
Database backups need to be stored in different physical locations to ensure data availability and protection against localized failures. Storing backups in multiple locations helps to safeguard against:

Natural Disasters: Events such as floods, earthquakes, or fires that could destroy data stored in a single location.
Hardware Failures: Issues such as disk failures that could corrupt or erase data.
Theft or Vandalism: Unauthorized access or damage to data storage facilities.
Data Corruption: Ensuring that at least one backup remains unaffected in case of corruption.
What operation should you regularly perform to make sure that your database backup strategy actually works?
To ensure that your database backup strategy actually works, you should regularly perform backup restoration tests. This involves:

Verifying Backups: Ensuring that backups are created correctly and are not corrupted.
Restoration Practice: Regularly restoring backups to a test environment to ensure that the process works smoothly.
Checking Data Integrity: Ensuring that the restored data is complete and accurate.
Documenting the Process: Keeping detailed records of the backup and restoration process, including any issues encountered and resolved.
