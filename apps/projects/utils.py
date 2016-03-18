from apps.questions.models import QuestionEntity


def get_question_entities(catalog):
    return QuestionEntity.objects \
        .filter(subsection__section__catalog=catalog) \
        .order_by('subsection__section__order', 'subsection__order', 'order')


def get_first_question_entity_id(catalog):
    return get_question_entities(catalog).first().pk


def get_previous_question_entity_id(catalog, current_question_entity_id):
    question_entity_id_list = list(get_question_entities(catalog).values_list('pk', flat=True))
    current_index = question_entity_id_list.index(current_question_entity_id)
    next_index = current_index - 1

    if next_index >= len(question_entity_id_list):
        return current_index
    else:
        return next_index


def get_next_question_entity_id(catalog, current_question_entity_id):
    question_entity_id_list = list(get_question_entities(catalog).values_list('pk', flat=True))
    current_index = question_entity_id_list.index(current_question_entity_id)
    next_index = current_index + 1

    if next_index >= len(question_entity_id_list):
        return current_index
    else:
        return next_index

# def check_condition(interview, condition):
#     try:
#         answer = Answer.objects.get(interview=interview, question=condition.question)
#     except Answer.DoesNotExist:
#         return True

#     if condition.relation == '>':
#         return (answer.value > condition.value)
#     elif condition.relation == '>=':
#         return (answer.value >= condition.value)
#     elif condition.relation == '<':
#         return (answer.value < condition.value)
#     elif condition.relation == '<=':
#         return (answer.value <= condition.value)
#     elif condition.relation == '==':
#         return (answer.value == condition.value)
#     elif condition.relation == '!=':
#         return (answer.value != condition.value)
#     else:
#         raise Exception('Unknown condition type.')


# def redirect_to_next_group(interview, group):
#     try:
#         interview.current_group = Group.objects.get_next(group)
#         interview.save()

#         return HttpResponseRedirect(reverse('interview_group', kwargs={
#             'interview_id': interview.pk,
#             'group_id': interview.current_group.pk
#         }))
#     except Group.DoesNotExist:
#         interview.current_group = None
#         interview.completed = True
#         interview.save()

#         return HttpResponseRedirect(reverse('interview_done', kwargs={
#             'interview_id': interview.pk
#         }))


# def fetch_answer_tree(interview):

#     answers_dict = {}
#     for answer in interview.answers.all():
#         answers_dict[answer.question.pk] = answer

#     answer_tree = []
#     for section in Section.objects.all():
#         section_node = {
#             'pk': section.pk,
#             'title': section.title,
#             'subsections': []
#         }

#         for subsection in section.subsections.all():
#             subsection_node = {
#                 'pk': subsection.pk,
#                 'title': subsection.title,
#                 'groups': []
#             }

#             for group in subsection.groups.all():

#                 skip = False
#                 for condition in group.conditions.all():
#                     if not check_condition(interview, condition):
#                         skip = True

#                 if not skip:
#                     group_node = {
#                         'pk': subsection.pk,
#                         'title': group.title,
#                         'questions': []
#                     }

#                     for question in group.questions.all():
#                         if question.pk in answers_dict:
#                             question_node = {
#                                 'pk': subsection.pk,
#                                 'text': question.text,
#                                 'answer': answers_dict[question.pk].text
#                             }
#                             group_node['questions'].append(question_node)

#                     if group_node['questions'] != []:
#                         subsection_node['groups'].append(group_node)

#             if subsection_node['groups'] != []:
#                 section_node['subsections'].append(subsection_node)

#         if section_node['subsections'] != []:
#             answer_tree.append(section_node)

#     return answer_tree
