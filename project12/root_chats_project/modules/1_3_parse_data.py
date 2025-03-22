'''
Gets saved json and splits data by fields
'''

import json

from load_django import *
from parser_app.models import *

for item in ConversationData.objects.filter(status='New'):
    conversation_json = json.loads(item.conversation_json)
    messages_json = json.loads(item.messages_json)
    
    item.contact_name = conversation_json['contact']['displayName']    
    item.contact_id = conversation_json['contact']['id']
    
    agents = []
    for agent_data in conversation_json['assignedUsers']:
        agent_name = agent_data['firstName'].strip()+ ' ' + agent_data['lastName'].strip()
        agents.append(agent_name)
    item.agents = agents
    
    labels = []
    for label_data in conversation_json['labels']:
        label = {}
        label['id'] = label_data['id']
        label['name'] = label_data['name']
        label['color'] = label_data['color']
        labels.append(label)
    item.labels = labels
    
    item.conversation_subject = conversation_json['subject']
    item.conversation_type = conversation_json['type']
    item.conversation_status = conversation_json['status']
    item.unread_count = conversation_json['unreadCount']
    item.archived_at = conversation_json['archivedAt']
    item.highlighted = conversation_json['highlighted']
    
    messages = []
    statuses = []
    for message_data in messages_json:
        message = {}
        if message_data['timelineType'] == 'MESSAGE':
            sent_by = message_data['sentBy']
            if sent_by:
                message['sent_by'] = sent_by['firstName'].strip() + ' ' + sent_by['lastName'].strip()
                
            message['id'] = message_data['id']
            message['text'] = message_data['payload']                      
            message['timestamp'] = message_data['timestamp']
            message['attachments'] = message_data['attachments']
            message['reactions'] = message_data['reactions']
            messages.append(message)
        status = {}                    
        if message_data['timelineType'] == 'CONVERSATION_STATUS':
            status['from']  = message_data['statusFrom']
            status['to'] = message_data['statusTo']
            status['timestamp'] = message_data['timestamp']
            changed_by = message_data['changedByUser']
            if changed_by:
                status['changed_by'] = changed_by['firstName'].strip() + ' ' + changed_by['lastName'].strip()
            statuses.append(status)
    item.messages = messages
    item.statuses = statuses
    
    item.status = 'Done'
    item.save()    
    print(item, 'Updated')
        