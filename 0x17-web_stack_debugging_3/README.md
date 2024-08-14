
# WordPress Apache Server Debugging

## Project Overview

This project involved debugging a WordPress website running on a LAMP stack (Linux, Apache, MySQL, PHP). The main task was to diagnose and resolve an issue where Apache was returning a `500 Internal Server Error` and to automate the fix using Puppet.

## Issues Encountered

### 1. Apache Returning 500 Internal Server Error

**Description:**  
Upon making an HTTP request to the local server (`http://127.0.0.1`), Apache returned a `500 Internal Server Error`. This error typically indicates a problem with the server configuration or a script being executed by Apache (e.g., PHP).

**Resolution:**  
- **Diagnostic Tool Used:** `strace` was utilized to trace system calls and signals received by the Apache process. This helped identify the root cause of the issue.
- **Solution:** Once the issue was identified, a Puppet manifest (`0-strace_is_your_friend.pp`) was created to automate the fix.

### 2. `strace` Permissions Issue

**Description:**  
When attempting to attach `strace` to an Apache process, the following error was encountered:

```plaintext
strace: Could not attach to process. If your uid matches the uid of the target process, check the setting of /proc/sys/kernel/yama/ptrace_scope, or try again as the root user. For more details, see /etc/sysctl.d/10-ptrace.conf: Operation not permitted
strace: attach: ptrace(PTRACE_SEIZE, 1167): Operation not permitted
```

**Resolution:**
- The issue was resolved by running `strace` as the root user using `sudo`.
- Alternatively, the `ptrace_scope` setting could be temporarily modified to allow non-root tracing by running `sudo sysctl -w kernel.yama.ptrace_scope=0`.

### 3. Apache Service Not Recognized

**Description:**  
The command to start the Apache2 service (`sudo service apache2 start`) resulted in the error `apache2: unrecognized service`.

**Resolution:**
- **For Ubuntu/Debian:** Apache2 was installed using `sudo apt-get install apache2`.
- **For CentOS/RHEL:** Apache was installed as `httpd` using `sudo yum install httpd`, and the service was started using `sudo service httpd start` or `sudo systemctl start httpd`.

### 4. Apache Not Running (No PID Found)

**Description:**  
When attempting to find the Apache process ID (PID), the process was not running, and thus no PID could be found.

**Resolution:**  
Apache was started using the appropriate service command (`sudo service apache2 start` or `sudo systemctl start apache2`), and the PID was retrieved using `ps aux | grep apache2`.

### 5. Successful Apache Status Check

**Description:**  
After starting Apache, a `curl` command to `http://127.0.0.1` returned a `200 OK` status, indicating the server was running correctly.

```plaintext
HTTP/1.1 200 OK
Date: Wed, 14 Aug 2024 10:49:47 GMT
Server: Apache/2.4.41 (Ubuntu)
Last-Modified: Wed, 14 Aug 2024 10:41:23 GMT
ETag: "2aa6-61fa25e0c8c50"
Accept-Ranges: bytes
Content-Length: 10918
Vary: Accept-Encoding
Content-Type: text/html
```

**Conclusion:**  
The Apache server was successfully debugged and is now serving content as expected.

## Automation with Puppet

A Puppet manifest (`0-strace_is_your_friend.pp`) was created to automate the fix for the `500 Internal Server Error`. This manifest ensures the Apache server is configured correctly and resolves the issue permanently.

## How to Use

1. **Start Apache:**  
   - Ubuntu/Debian: `sudo service apache2 start`
   - CentOS/RHEL: `sudo service httpd start`

2. **Check Apache Status:**
   - Run `curl -sI http://127.0.0.1` to verify the server is returning a `200 OK` status.

3. **Trace Apache Processes (if needed):**
   - Run `sudo strace -p <PID> -f -o /tmp/strace_output.log` to trace Apache processes for debugging.

4. **Apply Puppet Manifest:**
