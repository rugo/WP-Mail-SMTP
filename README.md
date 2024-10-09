# WP Mail SMTP
This script decrypts the SMTP password stored in a Wordpress database when the [WP Mail SMTP](https://wpmailsmtp.com) plugin is used.

The plugin stores the decryption key in the DB under the `wp_options` key `wp_mail_smtp_mail_key`.

Use like:

```bash
pip install -r requirements.txt
python3 $wp_mail_smtp_mail_key_pass $wp_mail_smtp_mail_key
```
