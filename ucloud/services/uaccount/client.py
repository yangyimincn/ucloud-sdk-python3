import typing


from ucloud.core.client import Client
from ucloud.services.uaccount.schemas import apis


class UAccountClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        super(UAccountClient, self).__init__(config, transport, middleware, logger)

    def create_project(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ CreateProject - 创建项目

        **Request**

        - **ProjectName** (str) - (Required) 项目名称
        
        **Response**

        - **ProjectId** (str) - 所创建项目的Id
        
        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.CreateProjectRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("CreateProject", d, **kwargs)
        return apis.CreateProjectResponseSchema().loads(resp)

    def get_project_list(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetProjectList - 获取项目列表

        **Request**

        - **IsFinance** (str) - 是否是财务账号(Yes: 是, No: 否)
        
        **Response**

        - **ProjectCount** (int) - 项目总数
        - **ProjectSet** (list) - 见 **ProjectListInfo** 模型定义
        
        **Response Model**
        
        **ProjectListInfo** 
        
        - **ResourceCount** (int) - 项目下资源数量
        - **MemberCount** (int) - 项目下成员数量
        - **ProjectId** (str) - 项目ID
        - **ProjectName** (str) - 项目名称
        - **ParentId** (str) - 父项目ID
        - **ParentName** (str) - 父项目名称
        - **CreateTime** (int) - 创建时间(Unix时间戳)
        - **IsDefault** (bool) - 是否为默认项目

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetProjectListRequestSchema().dumps(d)

        resp = self.invoke("GetProjectList", d, **kwargs)
        return apis.GetProjectListResponseSchema().loads(resp)

    def get_region(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetRegion - 获取用户在各数据中心的权限等信息

        **Request**

        
        **Response**

        - **Regions** (list) - 见 **RegionInfo** 模型定义
        
        **Response Model**
        
        **RegionInfo** 
        
        - **Region** (str) - 地域名字，如cn-bj
        - **Zone** (str) - 可用区名字，如cn-bj-01
        - **RegionId** (int) - 数据中心ID
        - **RegionName** (str) - 数据中心名称
        - **IsDefault** (bool) - 是否用户当前默认数据中心
        - **BitMaps** (str) - 用户在此数据中心的权限位

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetRegionRequestSchema().dumps(d)

        resp = self.invoke("GetRegion", d, **kwargs)
        return apis.GetRegionResponseSchema().loads(resp)

    def get_user_info(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetUserInfo - 获取用户信息

        **Request**

        
        **Response**

        - **DataSet** (list) - 见 **UserInfo** 模型定义
        
        **Response Model**
        
        **UserInfo** 
        
        - **Admin** (int) - 是否超级管理员 0:否 1:是
        - **Finance** (int) - 是否有财务权限 0:否 1:是
        - **UserEmail** (str) - 用户邮箱
        - **UserType** (int) - 会员类型
        - **Province** (str) - 省份
        - **AuthState** (str) - 实名认证状态
        - **UserId** (int) - 用户Id
        - **PhonePrefix** (str) - 国际号码前缀
        - **CompanyName** (str) - 公司名称
        - **IndustryType** (int) - 所属行业
        - **City** (str) - 城市
        - **UserAddress** (str) - 公司地址
        - **UserPhone** (str) - 用户手机
        - **UserName** (str) - 称呼
        - **UserVersion** (int) - 是否子帐户(大于100为子帐户)
        - **Administrator** (str) - 管理员

        """
        # build request
        d = {}
        req and d.update(req)
        d = apis.GetUserInfoRequestSchema().dumps(d)

        resp = self.invoke("GetUserInfo", d, **kwargs)
        return apis.GetUserInfoResponseSchema().loads(resp)

    def modify_project(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ModifyProject - 修改项目

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **ProjectName** (str) - (Required) 新的项目名称
        
        **Response**

        
        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.ModifyProjectRequestSchema().dumps(d)

        resp = self.invoke("ModifyProject", d, **kwargs)
        return apis.ModifyProjectResponseSchema().loads(resp)

    def terminate_project(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ TerminateProject - 删除项目

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        
        **Response**

        
        """
        # build request
        d = {"ProjectId": self.config.project_id}
        req and d.update(req)
        d = apis.TerminateProjectRequestSchema().dumps(d)

        resp = self.invoke("TerminateProject", d, **kwargs)
        return apis.TerminateProjectResponseSchema().loads(resp)
