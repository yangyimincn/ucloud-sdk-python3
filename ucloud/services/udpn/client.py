import typing


from ucloud.core.client import Client
from ucloud.services.udpn.schemas import apis


class UDPNClient(Client):
    def __init__(self, config: dict, transport=None, middleware=None, logger=None):
        super(UDPNClient, self).__init__(config, transport, middleware, logger)

    def allocate_udpn(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ AllocateUDPN - 分配一条 UDPN 专线

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Bandwidth** (int) - (Required) 带宽
        - **Peer1** (str) - (Required) 专线可用区1，支持地域：北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg,  洛杉矶：us-la， 华盛顿：us-ws， 东京：jpn-tky
        - **Peer2** (str) - (Required) 专线可用区2，支持地域：北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg,  洛杉矶：us-la， 华盛顿：us-ws， 东京：jpn-tky
        - **ChargeType** (str) - 计费类型，枚举值为： Year，按年付费； Month，按月付费； Dynamic，按需付费
        - **CouponId** (str) - 代金劵
        - **Quantity** (int) - 计费时长，默认 1
        
        **Response**

        - **UDPNId** (str) - 资源名称
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.AllocateUDPNRequestSchema().dumps(d)

        # build options
        kwargs["max_retries"] = 0  # ignore retry when api is not idempotent

        resp = self.invoke("AllocateUDPN", d, **kwargs)
        return apis.AllocateUDPNResponseSchema().loads(resp)

    def describe_udpn(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ DescribeUDPN - 描述 UDPN

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Limit** (int) - 返回数据长度，默认为 20
        - **Offset** (int) - 列表起始位置偏移量，默认为 0
        - **UDPNId** (str) - 申请到的 UDPN 资源 ID。若为空，则查询该用户在机房所有的专线信息。非默认项目资源，需填写ProjectId
        
        **Response**

        - **TotalCount** (int) - 查询到的总数量
        - **DataSet** (list) - 见 **UDPNData** 模型定义
        
        **Response Model**
        
        **UDPNData** 
        
        - **ExpireTime** (int) - unix 时间戳 到期时间
        - **UDPNId** (str) - UDPN 资源短 ID
        - **Peer1** (str) - 可用区域 1
        - **Peer2** (str) - 可用区域 2
        - **ChargeType** (str) - 计费类型
        - **Bandwidth** (int) - 带宽
        - **CreateTime** (int) - unix 时间戳 创建时间

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.DescribeUDPNRequestSchema().dumps(d)

        resp = self.invoke("DescribeUDPN", d, **kwargs)
        return apis.DescribeUDPNResponseSchema().loads(resp)

    def get_udpn_line_list(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetUDPNLineList - 获取当前支持的专线线路列表

        **Request**

        - **ProjectId** (str) - (Config) 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        
        **Response**

        - **TotalCount** (int) - DataSet中的元素个数
        - **DataSet** (list) - 见 **UDPNLineSet** 模型定义
        
        **Response Model**
        
        **UDPNLineSet** 
        
        - **BandwidthUpperLimit** (int) - 线路带宽上限,单位 M
        - **LocalRegion** (str) - 支持UDPN的地域之一，北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg, 华盛顿：us-ws, 洛杉矶：us-la， 东京：jpn-tky
        - **RemoteRegion** (str) - 支持UDPN的地域之一，北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg, 华盛顿：us-ws, 洛杉矶：us-la， 东京：jpn-tky

        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUDPNLineListRequestSchema().dumps(d)

        resp = self.invoke("GetUDPNLineList", d, **kwargs)
        return apis.GetUDPNLineListResponseSchema().loads(resp)

    def get_udpn_price(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ GetUDPNPrice - 获取 UDPN 价格

        **Request**

        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Bandwidth** (int) - (Required) 带宽信息
        - **Peer1** (str) - (Required) 专线可用区1，支持地域：北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg, 洛杉矶：us-la， 华盛顿：us-ws， 东京：jpn-tky
        - **Peer2** (str) - (Required) 专线可用区2，支持地域：北京二：cn-bj2, 上海二：cn-sh2, 广东：cn-gd, 亚太： hk, 上海一：cn-sh1, 法兰克福：ge-fra, 新加坡：sg, 洛杉矶：us-la， 华盛顿：us-ws， 东京：jpn-tky
        - **ChargeType** (str) - 计费类型
        - **Quantity** (int) - 购买时长
        
        **Response**

        - **PurchaseValue** (int) - 资源有效期 unix 时间戳
        - **Price** (float) - 专线价格
        
        """
        # build request
        d = {"Region": self.config.region}
        req and d.update(req)
        d = apis.GetUDPNPriceRequestSchema().dumps(d)

        resp = self.invoke("GetUDPNPrice", d, **kwargs)
        return apis.GetUDPNPriceResponseSchema().loads(resp)

    def get_udpn_upgrade_price(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ GetUDPNUpgradePrice - 获取专线升级价格

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Bandwidth** (int) - (Required) 带宽
        - **UDPNId** (str) - (Required) 专线带宽资源 Id
        
        **Response**

        - **Price** (float) - 升级后的价格
        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.GetUDPNUpgradePriceRequestSchema().dumps(d)

        resp = self.invoke("GetUDPNUpgradePrice", d, **kwargs)
        return apis.GetUDPNUpgradePriceResponseSchema().loads(resp)

    def modify_udpn_bandwidth(
        self, req: typing.Optional[dict] = None, **kwargs
    ) -> dict:
        """ ModifyUDPNBandwidth - 修改带宽值

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **Bandwidth** (int) - (Required) 调整后专线带宽, 单位为Mbps，取值范围为大于等于2且小于等于1000([2-1000])的整数
        - **UDPNId** (str) - (Required) UDPN Id
        - **CouponId** (str) - 代金劵 ID
        
        **Response**

        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ModifyUDPNBandwidthRequestSchema().dumps(d)

        resp = self.invoke("ModifyUDPNBandwidth", d, **kwargs)
        return apis.ModifyUDPNBandwidthResponseSchema().loads(resp)

    def release_udpn(self, req: typing.Optional[dict] = None, **kwargs) -> dict:
        """ ReleaseUDPN - 释放 UDPN

        **Request**

        - **ProjectId** (str) - (Config) 项目ID。不填写为默认项目，子帐号必须填写。 请参考 `GetProjectList接口 <https://docs.ucloud.cn/api/summary/get_project_list.html>`_ 
        - **Region** (str) - (Config) 地域。 参见  `地域和可用区列表 <https://docs.ucloud.cn/api/summary/regionlist.html>`_ 
        - **UDPNId** (str) - (Required) UDPN 资源 Id
        
        **Response**

        
        """
        # build request
        d = {"ProjectId": self.config.project_id, "Region": self.config.region}
        req and d.update(req)
        d = apis.ReleaseUDPNRequestSchema().dumps(d)

        resp = self.invoke("ReleaseUDPN", d, **kwargs)
        return apis.ReleaseUDPNResponseSchema().loads(resp)
