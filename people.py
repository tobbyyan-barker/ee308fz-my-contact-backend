#python 功能：指挥翻译官干活
from datetime import datetime
from flask import abort
from app import db, Contact # 导入翻译官"db" 和联系人列表"contact"


#辅助函数 作用: 返回当前时间
def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    #把字典转换为列表 为了显示方便
    return  list(PEOPLE.values())

def create(body): #增加联系人
    #1. connexion的魔法
    # "person" 这个参数是怎么来的呢?
    # connexion自动的: a.从requestBody 拿到json数据  b.检查它是否符合"person模板的规范" c.如果符合就把他转成python字典

    #2. 提取数据
    name = body.get("name","")
    phone = body.get("phone","") 

    #3.查找这个人的电话号码是否已经存在了
    existing_contact = Contact.query.filter_by(phone=phone).one_or_none()

    if existing_contact is None:
        #告诉翻译官按模板填好姓名，电话号码
        new_contact = Contact(name=name, phone=phone)
        #吧这个模板添加进来
        db.session.add(new_contact)
        #存储模板
        db.session.commit()

        return { "id": new_contact.id, "name": new_contact.name, "phone":new_contact.phone},201
    else:
        abort(409,f"phone number {phone} already existed")

def read_all(): #查read_all()
    contacts = Contact.query.all()

    contact_list = [] #最终返回给前端的从对象中提取到的所有列表
    #把对象列表转换成普通列表
    for contact in contacts:
        contact_list.append({ "id": contact.id, "name": contact.name, "phone": contact.phone })
    return contact_list

def read_one(person_id):
    #查person的id (GET/ people/ {person_id})
    contact = Contact.query.get_or_404(person_id)

    return { "id": contact.id, "name": contact.name, "phone":contact.phone}

def update(person_id,body):
    #改: 把原来(PUT/people/{person_id}) 然后最后的person_id转成新的person_id哈
    contact_to_update = Contact.query.get_or_404(person_id)
    contact_to_update.name = body.get("name")
    contact_to_update.phone = body.get("phone")

    db.session.commit()
    return { "id": contact_to_update.id, "name": contact_to_update.name, "phone":contact_to_update.phone},200

def delete(person_id):
    #删: 把原来(DELETE/people/{person_id}) 然后删除
    contact_to_delete = Contact.query.get_or_404(person_id)
    db.session.delete(contact_to_delete)
    db.session.commit()
    return "",204




