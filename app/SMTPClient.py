#from datetime import datetime
class SMTPClient:
    def send(subject, text, email_address) -> bool:
    #implementacja ktorej jeszcze nie mamy
    # return True jezeli wyslanie sie powiodło
    # return False jezeli wyslanie sie nie powiodło
        return False
    
    # def send_history_to_email(self, recipient_email, smtp_client):
    #     today = datetime.now().strftime("%Y-%m-%d")
    #     if self.account_type == "personal":
    #         subject = f"Wyciąg z dnia {today}"
    #         text = f"Twoja historia konta to: {self.history}"
    #     elif self.account_type == "business":
    #         subject = f"Wyciąg z dnia {today}"
    #         text = f"Historia konta Twojej firmy to: {self.history}"
    #     else:
    #         raise ValueError("Unsupported account type")

    #     return smtp_client.send(subject, text, recipient_email)
