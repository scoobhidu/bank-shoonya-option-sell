module.exports = {
  watch: true,
  watch_delay: 1000,
  apps: [
    {
      name: "fastapi-app",
      script: "uvicorn",
      args: "main:app --host 0.0.0.0 --port 8004", // Replace "main:app" with your app entry point
      cron_restart: "0 9 * * 1-5",
      // Environment configuration
      interpreter: "python3", // Ensure you're using the right Python version
      exec_mode: "fork",      // 'fork' mode for running a single instance
      instances: 1,           // Number of instances (can be more for clustering)

      // Optional logs
      out_file: "./logs/output.log",
      error_file: "./logs/error.log"
    }
  ]
};