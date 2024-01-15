import os
import json


class MessagesCounter():
    def __init__(self, identity, folder_path, file_name):
        self.identity = identity
        self.folder_path = folder_path
        self.file_name = file_name

        self.user_total_messages = 0


    def process_folder(self, folder_path):
        conversation_count = []

        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            if os.path.isdir(item_path):   
                counted_messages = self.count_sender_names(item_path)

                if (counted_messages[1]['Sum'] > 1):
                    conversation_count.append(counted_messages)

        return conversation_count


    def count_sender_names(self, folder_path):
        sender_names_count = {}
        sender_names_count['Sum'] = 0  
        conversation_name = None

        for filename in os.listdir(folder_path):
            if filename.endswith(".json"):
                file_path = os.path.join(folder_path, filename)

                with open(file_path, 'r') as file:
                    data = json.load(file)

                    if 'participants' in data:
                        participants = data['participants']

                        if len(participants) > 2 and conversation_name is None:
                            if 'title' in data:
                                conversation_name = data['title']
                            
                        for paricipant in participants:
                            if 'name' in paricipant:
                                paricipant_name = paricipant['name']

                                if paricipant_name not in sender_names_count:
                                    sender_names_count[paricipant_name] = 0

                    if 'messages' in data:
                        messages = data['messages']

                        for message in messages:
                            if 'sender_name' in message:
                                sender_name = message['sender_name']
                                sender_names_count['Sum'] += 1

                                if sender_name in sender_names_count:
                                    sender_names_count[sender_name] += 1

        self.user_total_messages += sender_names_count[self.identity]

        return conversation_name, sender_names_count


    def save_to_file(self, folder_path, file_name):
        sorted_results = sorted(self.process_folder(folder_path), key=lambda x: x[1]['Sum'], reverse=True)

        with open(f'{file_name}.txt', 'w', encoding='utf8') as file:
            file.write(f'{self.identity}\'s total number of messages: {self.user_total_messages}\n\n')

            for record in sorted_results:
                if record[0] is None:
                    for sender in record[1]:
                        file.write(f'{sender.encode('latin1').decode('utf8')}: {record[1][sender]} | ')
                    file.write('\n')

            file.write('\nGroup chats:\n\n')

            for record in sorted_results:
                if record[0] is not None:
                    file.write(f'"{record[0].encode('latin1').decode('utf8')}": ')            
                    for sender in record[1]:
                        file.write(f'{sender.encode('latin1').decode('utf8')}: {record[1][sender]} | ')
                    file.write('\n\n')  

    
    def generate_data(self):
        try:
            self.save_to_file(self.folder_path, self.file_name)
        except Exception as e:
            print(f"Error occurred: {e}")
            return False
        else:
            return True
